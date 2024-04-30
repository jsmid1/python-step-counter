from typing import Any

from ..complexities import (
    ComplexitiesDict,
    constant,
    linear_to_len,
)


bytearray_complexities: ComplexitiesDict = {
    '__add__': linear_to_len,
    '__alloc__': constant,
    '__contains__': linear_to_len,
    '__delattr__': constant,
    '__delitem__': linear_to_len,
    '__dir__': constant,
    '__eq__': linear_to_len,
    '__format__': linear_to_len,
    '__ge__': linear_to_len,
    '__getattribute__': constant,
    '__getitem__': constant,
    '__gt__': linear_to_len,
    '__iadd__': linear_to_len,
    '__imul__': linear_to_len,
    '__init__': linear_to_len,
    '__init_subclass__': constant,
    '__iter__': constant,
    '__le__': linear_to_len,
    '__len__': constant,
    '__lt__': linear_to_len,
    '__mod__': linear_to_len,
    '__mul__': linear_to_len,
    '__ne__': linear_to_len,
    '__new__': constant,
    '__reduce__': constant,
    '__reduce_ex__': constant,
    '__repr__': linear_to_len,
    '__rmul__': linear_to_len,
    '__setattr__': constant,
    '__setitem__': constant,
    '__sizeof__': constant,
    '__str__': linear_to_len,
    '__subclasshook__': constant,
    'append': constant,
    'capitalize': linear_to_len,
    'center': linear_to_len,
    'clear': constant,
    'copy': linear_to_len,
    'count': linear_to_len,
    'decode': linear_to_len,
    'endswith': linear_to_len,
    'expandtabs': linear_to_len,
    'extend': linear_to_len,
    'find': linear_to_len,
    'fromhex': linear_to_len,
    'hex': linear_to_len,
    'index': linear_to_len,
    'insert': linear_to_len,
    'isalnum': linear_to_len,
    'isalpha': linear_to_len,
    'isascii': linear_to_len,
    'isdigit': linear_to_len,
    'islower': linear_to_len,
    'isspace': linear_to_len,
    'istitle': linear_to_len,
    'isupper': linear_to_len,
    'join': linear_to_len,
    'ljust': linear_to_len,
    'lower': linear_to_len,
    'lstrip': linear_to_len,
    'maketrans': constant,
    'partition': linear_to_len,
    'pop': constant,
    'remove': linear_to_len,
    'removeprefix': linear_to_len,
    'removesuffix': linear_to_len,
    'replace': linear_to_len,
    'reverse': linear_to_len,
    'rfind': linear_to_len,
    'rindex': linear_to_len,
    'rjust': linear_to_len,
    'rpartition': linear_to_len,
    'rsplit': linear_to_len,
    'rstrip': linear_to_len,
    'split': linear_to_len,
    'splitlines': linear_to_len,
    'startswith': linear_to_len,
    'strip': linear_to_len,
    'swapcase': linear_to_len,
    'title': linear_to_len,
    'translate': linear_to_len,
    'upper': linear_to_len,
    'zfill': linear_to_len,
}