import builtins
import collections

from .builtins_py_def import builtins_py_method_defs
from .collections_py_def import collections_py_method_defs

from ..py_object import get_function_mapping

py_method_defs = {
    builtins: builtins_py_method_defs,
    collections: collections_py_method_defs,
}


def check_exist(module, class_):
    return module not in py_method_defs and class_ in py_method_defs[module]


def is_py_method_def(module, class_, method_name):
    return get_function_mapping(class_, method_name) is None and method_name in dir(
        class_
    )


def get_py_method_defs(module, class_):
    py_method_defs = set()
    for method_name in dir(class_):
        if is_py_method_def(module, class_, method_name):
            py_method_defs.add(method_name)

    return py_method_defs


def get_py_classes():
    return py_method_defs.keys()
