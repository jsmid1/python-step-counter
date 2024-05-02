from typing import Any
from ..complexities import (
    ComplexitiesDict,
    comparison_com,
    constant,
    linear_to_len,
    linear_to_len_sec,
    sequence_mul_complexity,
    sequence_join_complexity,
)


def bytes_add_complexity(args: tuple[Any, ...]) -> int:
    list_one = args[0]
    list_two = args[1]
    return len(list_one) + len(list_two)


bytes_complexities: ComplexitiesDict = {
    # Dunders
    '__add__': linear_to_len_sec,
    '__contains__': linear_to_len,
    '__getitem__': constant,
    '__hash__': linear_to_len,
    '__iter__': constant,
    '__len__': constant,
    '__mod__': linear_to_len,
    '__mul__': sequence_mul_complexity,
    '__repr__': linear_to_len,
    '__setattr__': constant,
    '__str__': linear_to_len,
    # Comparisons
    '__lt__': comparison_com,
    '__le__': comparison_com,
    '__eq__': comparison_com,
    '__ne__': comparison_com,
    '__gt__': comparison_com,
    '__ge__': comparison_com,
    # PyMethodDef
    'capitalize': linear_to_len,
    'center': linear_to_len,
    'count': linear_to_len,
    'decode': linear_to_len,
    'endswith': linear_to_len,
    'expandtabs': linear_to_len,
    'find': linear_to_len,
    'fromhex': linear_to_len,
    'hex': linear_to_len,
    'index': linear_to_len,
    'isalnum': linear_to_len,
    'isalpha': linear_to_len,
    'isascii': linear_to_len,
    'isdigit': linear_to_len,
    'islower': linear_to_len,
    'isspace': linear_to_len,
    'istitle': linear_to_len,
    'isupper': linear_to_len,
    'join': sequence_join_complexity,
    'ljust': linear_to_len,
    'lower': linear_to_len,
    'lstrip': linear_to_len,
    'maketrans': linear_to_len,
    'partition': linear_to_len,
    'removeprefix': linear_to_len,
    'removesuffix': linear_to_len,
    'replace': linear_to_len,
    'rfind': linear_to_len,
    'rindex': linear_to_len,
    'rjust': linear_to_len,
    'rpartition': linear_to_len,
    'rsplit': linear_to_len,
    'rstrip': linear_to_len,
    'split': linear_to_len,
    'splitlines': linear_to_len,
    'startswith': linear_to_len_sec,
    'strip': linear_to_len,
    'swapcase': linear_to_len,
    'title': linear_to_len,
    'translate': linear_to_len,
    'upper': linear_to_len,
    'zfill': linear_to_len,
}
