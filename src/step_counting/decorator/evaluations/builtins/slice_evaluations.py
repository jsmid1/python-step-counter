from typing import Any
from ..complexities import (
    ComplexitiesDict,
    comparison_com,
    constant,
    linear_to_len,
)


def slice_size_complexity(args: tuple[slice, ...]) -> int:
    slice_ = args[0]

    return (slice_.stop - slice_.start) // slice_.step


slice_complexities: ComplexitiesDict = {
    # Dunders
    '__repr__': slice_size_complexity,
    '__setattr__': constant,
    '__str__': slice_size_complexity,
    # Comparisons
    '__lt__': comparison_com,
    '__le__': comparison_com,
    '__eq__': comparison_com,
    '__ne__': comparison_com,
    '__gt__': comparison_com,
    '__ge__': comparison_com,
    # PyMethodDef
    'indices': constant,
}
