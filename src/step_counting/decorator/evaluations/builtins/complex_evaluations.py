from typing import Any, Callable
from ..complexities import constant

# TODO recheck, mul and pow are quite difficult
complex_complexities: dict[str, Callable[[tuple[Any, ...]], int]] = {
    '__add__': constant,
    '__sub__': constant,
    '__mul__': constant,
    '__pow__': constant,
    '__truediv__': constant,
    'conjugate': constant,
    'imag': constant,
    'real': constant,
}
