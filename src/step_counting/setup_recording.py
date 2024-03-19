import builtins
import ctypes
import inspect

from .decorator import decorators
from .non_builtin_types import (
    dict_items_type,
    dict_keys_type,
    dict_values_type,
    generator_type,
)
from .patch import patch_imports
from .patch import py_object as pyo
from .patch.patching import create_patch, apply, revert
from .original_methods import dict_items

from .utils.module import get_imports, is_user_defined_module, get_module_by_name


# TODO: Error handling!
def get_c_method(class_, method_name):
    tyobj = pyo.PyTypeObject.from_address(id(class_))
    method_mapping_info = pyo.get_function_mapping(class_, method_name)

    tp_name, c_method_name, type_ = method_mapping_info
    tp_as_ptr = getattr(tyobj, tp_name)
    if c_method_name is None:
        c_method = tp_as_ptr
    else:
        tp_as = tp_as_ptr[0]
        c_method = getattr(tp_as, c_method_name)

    py_type = ctypes.PYFUNCTYPE(*type_)
    method = ctypes.cast(c_method, py_type)
    return method


def decorate_all_py_method_def_mehods(decorator):
    for class_, methods in dict_items(pyo.py_method_def_by_class):
        for method_name in methods:
            create_patch(
                builtins,
                class_.__name__,
                method_name,
                decorator(getattr(class_, method_name), class_.__name__, method_name),
            )


py_object_method = {
    int: {
        '__repr__',
        'comparison',
        '__add__',
        '__sub__',
        '__mul__',
        '__mod__',
        '__divmod__',
        '__pow__',
        '__neg__',
        '__pos__',
        '__abs__',
        '__bool__',
        '__invert__',
        '__lshift__',
        '__rshift__',
        '__and__',
        '__xor__',
        '__or__',
        '__int__',
        '__float__',
        '__truediv__',
        '__index__',
    },
    float: {
        '__new__',
        '__init__',
        '__repr__',
        '__abs__',
        '__add__',
        '__bool__',
        '__float__',
        '__int__',
        '__mul__',
        '__neg__',
        '__pos__',
        '__pow__',
        '__repr__',
        '__sub__',
        '__truediv__',
        'comparison',
    },
    bool: {'__repr__', '__invert__', '__and__', '__xor__', '__or__'},
    str: {
        '__repr__',
        '__iter__',
        '__str__',
        '__len__',
        '__add__',
        '__mul__',
        '__getitem__',
        '__contains__',
        'comparison',
    },
    list: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__add__',
        '__mul__',
        '__getitem__',
        '__setitem__',
        '__contains__',
        '__iadd__',
        '__imul__',
    },
    set: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__and__',
        '__or__',
        '__xor__',
        '__sub__',
        '__contains__',
        '__iand__',
        '__ior__',
        '__ixor__',
        '__isub__',
    },
    frozenset: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__and__',
        '__or__',
        '__xor__',
        '__sub__',
        '__contains__',
    },
    bytes: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__add__',
        '__mul__',
        '__getitem__',
        '__contains__',
        '__mod__',
    },
    bytearray: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__add__',
        '__mul__',
        '__getitem__',
        '__setitem__',
        '__contains__',
        '__iadd__',
        '__imul__',
        '__mod__',
    },
    memoryview: {'__getitem__', '__iter__', '__len__', '__repr__', 'comparison'},
    complex: {
        '__repr__',
        'comparison',
        '__add__',
        '__sub__',
        '__mul__',
        '__truediv__',
        '__neg__',
        '__pos__',
        '__abs__',
        '__bool__',
        '__pow__',
    },
    tuple: {
        '__repr__',
        'comparison',
        '__iter__',
        '__len__',
        '__getitem__',
        '__contains__',
        '__add__',
        '__mul__',
    },
    dict: {
        '__repr__',
        '__hash__',
        'comparison',
        '__contains__',
        '__ior__',
        '__or__',
        '__len__',
        '__getitem__',
        '__setitem__',
    },
    range: {
        '__repr__',
        'comparison',
        '__iter__',
        '__bool__',
        '__len__',
        '__getitem__',
        '__contains__',
    },
    enumerate: {'__iter__'},
    generator_type: {
        '__iter__',
    },  #'tp_iternext'
    dict_keys_type: {'__contains__', '__iter__', '__len__', '__and__', 'comparison'},
    dict_values_type: {'__iter__', '__len__'},
    dict_items_type: {'__contains__', '__iter__', '__len__', 'comparison'},
    # class_type: {'__init__'},
}


def decorate_all_py_object_methods(decorator):
    for class_, method_list in py_object_method.items():
        for method_name in method_list:
            try:
                original_method = get_c_method(class_, method_name)
                replacement_method = decorator(
                    original_method, class_.__name__, method_name
                )
                create_patch(
                    builtins,
                    class_.__name__,
                    method_name,
                    replacement_method,
                )
            except Exception:
                raise Exception(
                    f'Failed while patching method {method_name} of class {class_.__name__}!',
                    Exception,
                )

    decorate_all_py_method_def_mehods(decorator)


def decorate_all_methods_in_module(module, decorator):
    for name, obj in inspect.getmembers(module):

        # inspect.isfunction only works for user define functions
        # therefore we use callable(obj)
        if callable(obj):
            create_patch(module, None, name, decorator(obj, obj.__name__, name))

        if inspect.isclass(obj) and obj.__name__ != 'BuiltinImporter':
            for name, fn in inspect.getmembers(obj, predicate=inspect.isfunction):
                create_patch(
                    module,
                    obj.__name__,
                    name,
                    decorator(fn, obj.__name__, name),
                )


def wrap_import(decorator):
    import_wrapper = patch_imports.wrap_it('__import__', patch_imports.wrap_import)
    setattr(builtins, '__import__', decorator(import_wrapper, 'builtins', '__import__'))


def patch_imported_methods(imported_methods, decorator):
    for method in imported_methods:
        create_patch(
            get_module_by_name(method.__module__),
            None,
            method.__name__,
            decorator(method, None, method.__name__),
        )


def setup_recording(module, ignored_modules):
    module_imports, imported_methods = get_imports(module)
    module_imports = [
        import_ for import_ in module_imports if import_.__name__ not in ignored_modules
    ]
    user_defined_modules = [
        import_ for import_ in module_imports if is_user_defined_module(import_)
    ] + [module]

    decorator, recorder = decorators.create_decorator_detail(
        [module.__name__ for module in user_defined_modules]
    )

    wrap_import(decorator)

    patch_imported_methods(imported_methods, decorator)

    for module in module_imports:
        decorate_all_methods_in_module(module, decorator)

    decorate_all_py_object_methods(decorator)

    return recorder, user_defined_modules


class recording_activated:
    def __enter__(self):
        apply()

    def __exit__(self, type, value, traceback):
        revert()
