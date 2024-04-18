from types import ModuleType
from typing import Any, Callable
from .utils.module import get_imports, is_user_defined_module
from . import setup_recording

ignored_object_methods = {
    '__class__',
    '__dir__',
    '__getattribute__',
    '__hash__',
    '__init__',
    '__new__',
    '__delattr__',
    '__doc__',
    '__getnewargs__',
    '__init_subclass__',
    '__reduce__',
    '__reduce_ex__',
    '__sizeof__',
    '__subclasshook__',
    '__delitem__',
    '__alloc__',
    '__setformat__',
    '__setitem__',
    '__format__',  # Can be removed after fix in restrict.
}

comparison_operations = {'__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__ne__'}

ignored_r_methods = {
    '__radd__',
    '__rand__',
    '__rdivmod__',
    '__rfloordiv__',
    '__rlshift__',
    '__rmod__',
    '__rmul__',
    '__ror__',
    '__rpow__',
    '__rrshift__',
    '__rsub__',
    '__rtruediv__',
    '__rxor__',
}

ignored_methods = set.union(
    ignored_object_methods, comparison_operations, ignored_r_methods
)

ignored_specifics = {
    (dict, '__iter__'),
    (dict, '__setitem__'),
    (memoryview, 'itemsize'),
}

ignored_classes = {'BuiltinImporter'}

ignored_class_methods = {'__init__', '__new__'}


def get_def_ignored_modules() -> tuple[set[ModuleType], set[Callable[..., Any]]]:
    setup_modules, setup_callables = get_imports(setup_recording)
    setup_modules = {
        module for module in setup_modules if is_user_defined_module(module)
    }

    return setup_modules, setup_callables
