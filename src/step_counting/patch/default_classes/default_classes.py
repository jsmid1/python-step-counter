import builtins
import collections
from types import ModuleType
from typing import Iterable

from .builtins_py_def import builtins_py_method_defs
from .collections_py_def import collections_py_method_defs

from ..py_object import get_function_mapping

py_method_defs = {
    builtins: builtins_py_method_defs,
    collections: collections_py_method_defs,
}


def is_py_method_def(module: ModuleType, class_: type, method_name: str) -> bool:
    return get_function_mapping(class_, method_name) is None and method_name in dir(
        class_
    )


def get_py_method_defs(module: ModuleType, class_: type) -> set[str]:
    py_method_defs = set()
    for method_name in dir(class_):
        if is_py_method_def(module, class_, method_name):
            py_method_defs.add(method_name)

    return py_method_defs


def get_py_classes() -> Iterable[ModuleType]:
    return py_method_defs.keys()
