from ..evaluations.evaluations import evaluate_record
from ...original_methods import (
    int_add,
    list_append,
    dict_get,
    dict_setitem,
    dict_contains,
)


class counter:
    def __init__(self, count=0, evaluation=0) -> None:
        self.count_total = count
        self.evaluation_total = evaluation

    def increase(self, evaluation_total):
        self.count_total = int_add(self.count_total, 1)
        self.evaluation_total = int_add(self.evaluation_total, evaluation_total)

    def get_count_total(self):
        return self.count_total

    def get_evaluation_total(self):
        return self.evaluation_total

    def clear(self):
        self.count_total = 0
        self.evaluation_total = 0

    def __str__(self):
        return f'(Counter {self.count_total}, {self.evaluation_total})'


class simple_call_recorder:
    def __init__(self):
        self.counter = counter()

    def add_record(self, cls, func_name, arguments):
        self.counter.increase(record_eval)

    def get_data(self):
        return self.counter

    def evaluate_data(self):
        return self.counter.get_evaluation_total()

    def clear_data(self):
        self.counter.clear()


class sequence_call_recorder:
    def __init__(self):
        self.records = []

    def add_record(self, module_name, class_name, func_name):
        list_append(self.records, (module_name, class_name, func_name))

    def get_data(self):
        return self.records.copy()

    def evaluate_data(self):
        return len(self.records)

    def clear_data(self):
        self.records.clear()


class detail_call_recorder:
    def __init__(self):
        self.records = dict()

    def add_record(self, module_name, line_number, cls, func_name, arguments):
        record_eval = evaluate_record(cls, func_name, arguments)
        module_records = dict_get(self.records, module_name, None)

        if module_records is None:
            dict_setitem(
                self.records,
                module_name,
                {line_number: {(cls, func_name): counter(1, record_eval)}},
            )
            return

        line_records = dict_get(module_records, line_number, None)
        if line_records is None:
            dict_setitem(
                module_records,
                line_number,
                {(cls, func_name): counter(1, record_eval)},
            )
            return

        method_counter = dict_get(line_records, (cls, func_name), None)
        if method_counter is None:
            method_counter = counter()

        method_counter.increase(record_eval)
        dict_setitem(line_records, (cls, func_name), method_counter)

    def get_data(self):
        return self.records.copy()

    def evaluate_data(self):
        score = 0
        for module_records in self.records.values():
            for line_records in module_records.values():
                for counter_ in line_records.values():
                    score += counter_.get_evaluation_total()

        return score

    def clear_data(self):
        self.records.clear()
