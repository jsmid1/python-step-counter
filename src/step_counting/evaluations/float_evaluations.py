from .complexities import constant, logarithmic_to_sec


float_complexities = {
    '__add__': constant,
    '__and__': constant,
    '__floordiv__': constant,
    '__invert__': constant,
    '__lshift__': constant,
    '__mod__': constant,
    '__mul__': constant,  # TODO recheck
    '__neg__': constant,
    '__or__': constant,
    '__pow__': logarithmic_to_sec,  # TODO: Karatsuba algorithm make be used on large numbers
    '__rshift__': constant,
    '__sub__': constant,
    '__truediv__': constant,
    '__xor__': constant,
    'conjugate': constant,
    'imag': constant,
    'numerator': constant,
    'real': constant,
}
