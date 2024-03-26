import builtins
import collections

from .builtins_py_def import builtins_py_method_defs
from .collections_py_def import collections_py_method_defs

py_method_defs = {
    builtins: builtins_py_method_defs,
    collections: collections_py_method_defs,
}


def check_exist(module, class_):
    if module not in py_method_defs:
        return False
        raise Exception(f'Module {module.__name__} is not a default module')

    if class_ not in py_method_defs[module]:
        return False
        raise Exception(f'Class {class_} is not a default class')

    return True


def is_py_method_def(module, class_, method_name):
    return check_exist(module, class_) and method_name in py_method_defs[module][class_]


def get_py_method_defs(module, class_):
    if check_exist(module, class_):
        return None

    return py_method_defs.get(class_)


def get_py_classes():
    return py_method_defs.keys()
