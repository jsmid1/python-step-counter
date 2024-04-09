from typing import Any

from ..complexities import ComplexitiesDict, constant, linear_to_len


def set_or_complexity(args: tuple[Any, ...]) -> int:
    sequence_one = args[0]
    sequence_two = args[1]

    return len(sequence_one) + len(sequence_two)


def min_len_complexity(args: tuple[Any, ...]) -> int:
    set_one = args[0]
    set_two = args[1]
    return min(len(set_one), len(set_two))


def sum_len_complexity(args: tuple[Any, ...]) -> int:
    set_one = args[0]
    set_two = args[1]
    return len(set_one) + len(set_two)


def sum_len_list_complexity(args: tuple[Any, ...]) -> int:
    set_list = args[0]
    return sum(len(set_) for set_ in set_list)


def set_difference_complexity(args: tuple[Any, ...]) -> int:
    set_list = args
    return sum(len(set_) for set_ in set_list)


set_complexities: ComplexitiesDict = {
    '__len__': constant,
    '__contains__': linear_to_len,
    '__sub__': linear_to_len,
    '__or__': set_or_complexity,
    '__and__': min_len_complexity,
    '__xor__': set_or_complexity,
    '__iter__': constant,
    'add': constant,
    'clear': linear_to_len,
    'copy': linear_to_len,
    'difference': set_difference_complexity,
    'difference_update': set_difference_complexity,
    'discard': constant,
    'intersection': min_len_complexity,
    'intersection_update': min_len_complexity,
    'isdisjoint': min_len_complexity,
    'issubset': min_len_complexity,
    'issuperset': min_len_complexity,
    'pop': constant,
    'remove': constant,
    'symmetric_difference': sum_len_complexity,
    'symmetric_difference_update': sum_len_complexity,
    'union': sum_len_complexity,
    'update': sum_len_complexity,
}
