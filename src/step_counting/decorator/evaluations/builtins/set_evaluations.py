from typing import Any

from ..complexities import (
    ComplexitiesDict,
    constant,
    hash_complexity_sec,
    linear_to_len,
    comparison_com,
    linear_to_len_sec,
    linear_to_len_sum,
)


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
    # Dunders
    '__and__': linear_to_len_sec,
    '__class_getitem__': constant,
    '__contains__': hash_complexity_sec,
    '__iand__': linear_to_len_sec,
    '__ior__': linear_to_len_sum,
    '__isub__': linear_to_len_sec,
    '__iter__': constant,
    '__ixor__': linear_to_len_sum,
    '__len__': constant,
    '__or__': linear_to_len_sum,
    '__repr__': linear_to_len,
    '__setattr__': constant,
    '__str__': linear_to_len,
    '__sub__': linear_to_len_sec,
    '__xor__': linear_to_len_sum,
    # Comparisons
    '__lt__': comparison_com,
    '__le__': comparison_com,
    '__eq__': comparison_com,
    '__ne__': comparison_com,
    '__gt__': comparison_com,
    '__ge__': comparison_com,
    # PyMethodDef
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
