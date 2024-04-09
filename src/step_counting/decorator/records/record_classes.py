from types import ModuleType
from typing import Any, Optional
from ..evaluations.evaluations import evaluate_record

from ...original_methods import dict_get, list_append

########################################################################################
# These methods are used with patches applied. Even through it is not necessary
# to use original methods, they are used for optimization.
########################################################################################


class counter:
    def __init__(self, count: int = 0, evaluation: int = 0) -> None:
        self.count_total = count
        self.evaluation_total = evaluation

    def increase(self, evaluation_total: int) -> None:
        self.count_total = int.__add__(self.count_total, 1)
        self.evaluation_total = int.__add__(self.evaluation_total, evaluation_total)

    def get_count_total(self) -> int:
        return self.count_total

    def get_evaluation_total(self) -> int:
        return self.evaluation_total

    def clear(self) -> None:
        self.count_total = 0
        self.evaluation_total = 0

    def __str__(self) -> str:
        return f'(Counter {self.count_total}, {self.evaluation_total})'


class simple_call_recorder:
    def __init__(self) -> None:
        self.counter = counter()

    def add_record(self, cls: type, func_name: str, arguments: Any) -> None:
        self.counter.increase(evaluate_record(cls.__name__, func_name, arguments))

    def get_data(self) -> counter:
        return self.counter

    def evaluate_data(self) -> int:
        return self.counter.get_evaluation_total()

    def clear_data(self) -> None:
        self.counter.clear()


class sequence_call_recorder:
    def __init__(self) -> None:
        self.records: list[tuple[ModuleType, str, str]] = []

    def add_record(self, module: ModuleType, class_name: str, func_name: str) -> None:
        list_append(self.records, (module, class_name, func_name))

    def get_data(self) -> list[tuple[ModuleType, str, str]]:
        return self.records.copy()

    def evaluate_data(self) -> int:
        return len(self.records)

    def clear_data(self) -> None:
        self.records.clear()


class detail_call_recorder:
    def __init__(self) -> None:
        self.records: dict[ModuleType, dict[int, dict[tuple[str, str], counter]]] = (
            dict()
        )

    def add_record(
        self,
        module: ModuleType,
        line_number: int,
        cls: type,
        func_name: str,
        arguments: Any,
    ) -> None:
        record_eval = evaluate_record(cls.__name__, func_name, arguments)
        module_records = dict_get(self.records, module, None)

        if module_records is None:
            records: dict[int, dict[tuple[type, str], counter]] = {
                line_number: {(cls, func_name): counter(1, record_eval)}
            }
            dict.__setitem__(
                # mypy gets confused with dunder method use
                self.records,
                module,  # type: ignore
                records,
            )
            return

        # mypy gets confused with dunder method use
        line_records: Optional[dict[tuple[type, str], counter]] = dict_get(
            module_records, line_number, None
        )  # type: ignore
        if line_records is None:
            dict.__setitem__(
                module_records,
                # mypy gets confused with dunder method use
                line_number,  # type: ignore
                {(cls, func_name): counter(1, record_eval)},
            )
            return

        method_counter = dict_get(line_records, (cls, func_name), None)
        if method_counter is None:
            method_counter = counter()

        method_counter.increase(record_eval)
        dict.__setitem__(line_records, (cls, func_name), method_counter)

    def get_data(
        self,
    ) -> dict[ModuleType, dict[int, dict[tuple[str, str], counter]]]:
        return self.records.copy()

    def evaluate_data(self) -> int:
        score = 0
        for module_records in self.records.values():
            for line_records in module_records.values():
                for counter_ in line_records.values():
                    score += counter_.get_evaluation_total()

        return score

    def clear_data(self) -> None:
        self.records.clear()
