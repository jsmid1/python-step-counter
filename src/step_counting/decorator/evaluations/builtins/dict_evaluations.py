from typing import Any
from ..complexities import (
    ComplexitiesDict,
    constant,
    hash_complexity_sec,
    linear_to_len,
    comparison_com,
)


def dict_update_complexity(args: tuple[dict[Any, Any], dict[Any, Any]]) -> int:
    dict_one = args[0]
    dict_two = args[1]
    return len(dict_one) + len(dict_two)


dict.__reversed__
dict_complexities: ComplexitiesDict = {
    # Dunders
    '__class_getitem__': constant,
    '__contains__': hash_complexity_sec,
    '__getitem__': hash_complexity_sec,
    '__ior__': linear_to_len,
    '__len__': constant,
    '__or__': linear_to_len,
    '__repr__': linear_to_len,
    '__reversed__': constant,
    '__setattr__': constant,
    '__setitem__': hash_complexity_sec,
    '__str__': linear_to_len,
    # Comparisons
    '__lt__': comparison_com,
    '__le__': comparison_com,
    '__eq__': comparison_com,
    '__ne__': comparison_com,
    '__gt__': comparison_com,
    '__ge__': comparison_com,
    # PyMethodDef
    'clear': linear_to_len,
    'copy': linear_to_len,
    'fromkeys': linear_to_len,
    'get': constant,
    'items': linear_to_len,
    'keys': linear_to_len,
    'pop': constant,
    'popitem': constant,
    'setdefault': constant,
    'update': dict_update_complexity,
    'values': linear_to_len,
}
