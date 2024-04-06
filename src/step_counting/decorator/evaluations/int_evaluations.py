from .complexities import (
    constant,
    logarithmic,
    linear,
    linear_to_sec,
    quadratic,
)


def linear_to_len(args):
    return len(args[0])


def quadratic_to_bit_len(args):
    n = args[0]
    return 5


int_complexities = {
    '__add__': constant,
    '__and__': constant,
    '__floordiv__': constant,
    '__invert__': constant,
    '__lshift__': constant,
    '__mod__': constant,
    '__mul__': quadratic,
    '__neg__': constant,
    '__or__': constant,
    '__pow__': linear_to_sec,  # TODO: Karatsuba algorithm make be used on large numbers
    '__rshift__': constant,
    '__sub__': constant,
    '__truediv__': constant,
    '__xor__': constant,
    'bit_length': logarithmic,
    'conjugate': constant,
    'from_bytes': linear_to_len,
    'to_bytes': logarithmic,
}
