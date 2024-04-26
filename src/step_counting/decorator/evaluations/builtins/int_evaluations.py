from typing import Any, Callable, Literal, Sequence
from ..complexities import (
    ComplexitiesDict,
    constant,
    logarithmic,
    linear,
    linear_to_sec,
    quadratic,
)


def linear_to_len(args: tuple[Sequence[Any]]) -> int:
    return len(args[0])


# TODO finish
def quadratic_to_bit_len(args: tuple[int]) -> int:
    n = args[0]
    return n.bit_length()


int_complexities: ComplexitiesDict = {
    '__add__': constant,
    '__and__': constant,
    '__floordiv__': constant,
    '__invert__': constant,
    '__lshift__': constant,
    '__mod__': constant,
    '__mul__': constant,
    '__neg__': constant,
    '__or__': constant,
    '__pow__': linear_to_sec,  # Karatsuba algorithm may be used on large numbers
    '__rshift__': constant,
    '__sub__': constant,
    '__truediv__': constant,
    '__xor__': constant,
    'bit_length': logarithmic,
    'conjugate': constant,
    'from_bytes': linear_to_len,
    'to_bytes': logarithmic,
}
