from typing import Any, Callable, Literal, Sequence
from ..complexities import (
    ComplexitiesDict,
    constant,
    linear_to_bit_len,
    logarithmic,
    linear,
    linear_to_sec,
    logarithmic_to_sec,
    quadratic,
)


def linear_to_len(args: tuple[Sequence[Any]]) -> int:
    return len(args[0])


def quadratic_to_bit_len(args: tuple[int]) -> int:
    n = args[0]
    return n.bit_length() ** 2


int_complexities: ComplexitiesDict = {
    '__abs__': constant,
    '__add__': constant,
    '__and__': constant,
    '__bool__': constant,
    '__ceil__': constant,
    '__divmod__': constant,
    '__float__': constant,
    '__floor__': constant,
    '__floordiv__': constant,
    '__hash__': constant,
    '__index__': constant,
    '__int__': constant,
    '__invert__': constant,
    '__lshift__': constant,
    '__mod__': constant,
    '__mul__': constant,
    '__neg__': constant,
    '__or__': constant,
    '__pos__': constant,
    '__pow__': logarithmic_to_sec,
    '__repr__': constant,
    '__round__': constant,
    '__rshift__': linear_to_bit_len,
    '__setattr__': constant,
    '__str__': constant,
    '__sub__': constant,
    '__truediv__': constant,
    '__trunc__': constant,
    '__xor__': linear_to_bit_len,
    'as_integer_ratio': linear_to_bit_len,
    'bit_count': linear_to_bit_len,
    'bit_length': linear_to_bit_len,
    'conjugate': constant,
    'denominator': constant,
    'from_bytes': linear_to_len,
    'imag': constant,
    'numerator': constant,
    'real': constant,
    'to_bytes': linear_to_bit_len,
    'comparison': constant,
}
