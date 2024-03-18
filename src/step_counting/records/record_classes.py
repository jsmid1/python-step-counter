from ..evaluations import evaluations

int_add = int.__add__
list_append = list.append
list_getitem = list.__getitem__
dict_get = dict.get
dict_getitem = dict.__getitem__
dict_setitem = dict.__setitem__
tuple_getitem = tuple.__getitem__
dict_keys = dict.keys
dict_values = dict.values


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

    def __str__(self):
        return f'(Counter {self.count_total}, {self.evaluation_total})'


class simple_call_recorder:
    def __init__(self):
        self.records = {}

    def add_record(self, cls, func_name, arguments):
        counter_ = dict_get(self.records, (cls, func_name), None)
        if counter_ is None:
            counter_ = counter()

        counter_.increase(evaluations.evaluate_record(cls, func_name, arguments))
        dict_setitem(self.records, (cls, func_name), counter_)

    def get_data(self):
        return self.records.copy()

    def evaluate_data(self):
        total = 0
        for counter_ in self.records.values():
            total = int_add(total, counter_.get_evaluation_total())

        return total

    def clear_data(self):
        self.records.clear()


class sequence_call_recorder:
    def __init__(self):
        self.records = []

    def add_record(self, cls, func_name, arguments):
        list_append(
            self.records,
            (cls, func_name, evaluations.evaluate_record(cls, func_name, arguments)),
        )

    def get_data(self):
        return self.records

    def evaluate_data(self):
        return sum([evaluation for _, _, evaluation in self.records])

    def clear_data(self):
        self.records.clear()


_print = print


class detail_call_recorder:
    def __init__(self):
        self.records = {}

    def add_record(self, module_name, line_number, cls, func_name, arguments):
        module_records = dict_get(self.records, module_name, None)

        if module_records is None:
            dict_setitem(
                self.records,
                module_name,
                {
                    line_number: {
                        (cls, func_name): counter(
                            1, evaluations.evaluate_record(cls, func_name, arguments)
                        )
                    }
                },
            )
            return

        line_records = dict_get(module_records, line_number, None)
        if line_records is None:
            dict_setitem(
                module_records,
                line_number,
                {
                    (cls, func_name): counter(
                        1, evaluations.evaluate_record(cls, func_name, arguments)
                    )
                },
            )
            return

        method_counter = dict_get(line_records, (cls, func_name), None)
        if method_counter is None:
            method_counter = counter()
        method_counter.increase(evaluations.evaluate_record(cls, func_name, arguments))
        dict_setitem(line_records, (cls, func_name), method_counter)

    def get_data(self):
        return self.records

    def evaluate_data(self):
        score = 0
        for module_records in self.records.values():
            for line_records in module_records.values():
                for counter_ in line_records.values():
                    score = int_add(score, counter_.get_evaluation_total())

        return score

    def clear_data(self):
        self.records.clear()
