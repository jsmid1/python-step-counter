from typing import Any, Callable, Literal
from .builtins_evaluations import builtins_complexities
from .bytes_evaluations import bytes_complexities
from .complex_evaluations import complex_complexities
from .dict_evaluations import dict_complexities
from .float_evaluations import float_complexities
from .int_evaluations import int_complexities
from .list_evaluations import list_complexities
from .set_evaluations import set_complexities
from .str_evaluations import str_complexities


# TODO fill in complexities for other types
evaluation_method: dict[str, dict[str, Callable[[tuple[Any, ...]], int]]] = {
    'builtins': builtins_complexities,
    'bytes': bytes_complexities,
    'complex': complex_complexities,
    'dict': dict_complexities,
    'float': float_complexities,
    'int': int_complexities,
    'list': list_complexities,
    'set': set_complexities,
    'str': str_complexities,
}


def default_evaluation(_: Any) -> Literal[1]:
    return 1


def get_evaluation_method(
    cls_name: str, func_name: str
) -> Callable[[tuple[Any, ...]], int]:
    return evaluation_method.get(cls_name, {}).get(func_name, default_evaluation)


def evaluate_record(cls: str, func_name: str, args: tuple[Any, ...]) -> int:
    if func_name == '__import__':
        return 1

    return get_evaluation_method(cls, func_name)(args)
