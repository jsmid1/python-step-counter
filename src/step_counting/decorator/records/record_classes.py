from types import ModuleType
from typing import Any, Callable, Optional, TypeAlias

from src.step_counting.utils.module import get_module_by_name
from ..evaluations.evaluations import evaluate_record

from ...original_methods import dict_get, list_append

RecordKey: TypeAlias = tuple[ModuleType, Optional[type], str]
SequenceRecords: TypeAlias = list[tuple[ModuleType, str, str]]
ModuleDetailRecords: TypeAlias = dict[int, dict[RecordKey, 'Counter']]
DetailRecords: TypeAlias = dict[ModuleType, ModuleDetailRecords]
########################################################################################
# These methods are used with patches applied. Even through it is not necessary
# to use original methods, they are used for optimization.
########################################################################################


class Counter:
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


class SimpleCallRecorder:
    def __init__(self) -> None:
        self.counter = Counter()

    def add_record(
        self,
        orig_module: ModuleType,
        cls: Optional[type],
        func_name: str,
        arguments: Any,
    ) -> None:
        self.counter.increase(evaluate_record(orig_module, cls, func_name, arguments))

    def get_data(self) -> Counter:
        return self.counter

    def evaluate_data(self) -> int:
        return self.counter.get_evaluation_total()

    def clear_data(self) -> None:
        self.counter.clear()


class SequnceCallRecorder:
    def __init__(self) -> None:
        self.records: SequenceRecords = []

    def add_record(
        self, module: ModuleType, class_: Optional[type], func_name: str
    ) -> None:
        list_append(self.records, (module, class_, func_name))  # type: ignore

    def get_data(self) -> list[tuple[ModuleType, str, str]]:
        return self.records.copy()

    def evaluate_data(self) -> int:
        return len(self.records)

    def clear_data(self) -> None:
        self.records.clear()


class DetailCallRecorder:
    def __init__(self) -> None:
        self.records: DetailRecords = dict()

    def add_record(
        self,
        module: ModuleType,
        line_number: int,
        orig_module: ModuleType,
        cls: Optional[type],
        func: Callable[..., Any],
        func_name: str,
        arguments: Any,
    ) -> None:

        fn_class = getattr(func, '__objclass__', cls)
        fn_module_name = getattr(fn_class, '__module__', None)
        fn_module = get_module_by_name(fn_module_name) if fn_module_name else module

        record_eval = evaluate_record(fn_module, fn_class, func_name, arguments)
        module_records = dict_get(self.records, module, None)

        if module_records is None:
            records: dict[int, dict[RecordKey, Counter]] = {
                line_number: {(orig_module, cls, func_name): Counter(1, record_eval)}
            }
            dict.__setitem__(
                # mypy gets confused with dunder method use
                self.records,
                module,
                records,
            )
            return

        # mypy gets confused with dunder method use
        line_records: Optional[dict[tuple[type, str], Counter]] = dict_get(
            module_records, line_number, None
        )  # type: ignore
        if line_records is None:
            dict.__setitem__(
                module_records,
                # mypy gets confused with dunder method use
                line_number,
                {(orig_module, cls, func_name): Counter(1, record_eval)},
            )
            return

        method_counter = dict_get(line_records, (orig_module, cls, func_name), None)  # type: ignore
        if method_counter is None:
            method_counter = Counter()

        method_counter.increase(record_eval)
        dict.__setitem__(line_records, (orig_module, cls, func_name), method_counter)  # type: ignore

    def get_data(self) -> DetailRecords:
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
