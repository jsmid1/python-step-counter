import builtins
import collections
import inspect

from .decorator import decorators
from .non_builtin_types import (
    dict_items_type,
    dict_keys_type,
    dict_values_type,
    generator_type,
    dict_iter_type,
    list_iter_type,
    tuple_iter_type,
)

from .ignor import get_ignored_methods
from .patch import patch_imports
from .patch import py_object as pyo
from .patch.default_classes.default_classes import get_py_method_defs, is_py_method_def
from .patch.patching import create_patch, apply, revert
from .original_methods import dict_items

from .utils.module import get_imports, is_user_defined_module, get_module_by_name
from .utils.utils import get_c_method

py_objects = {
    builtins: {
        int,
        float,
        complex,
        dict,
        list,
        bool,
        str,
        set,
        frozenset,
        bytes,
        bytearray,
        str,
        memoryview,
        tuple,
        slice,
        range,
        dict_items_type,
        dict_keys_type,
        dict_values_type,
    },
    collections: {
        collections.deque,
    },
}

builtin_methods = [
    'print',
    'AssertionError',
    #'AttributeError',
    #'hasattr',
    'sum',
    'enumerate',
    '__build_class__',
    # 'isinstance',
    'open',
    #
    'print',
    '__build_class__',
    '__debug__',
    '__doc__',
    '__loader__',
    '__name__',
    '__package__',
    '__spec__',
    'aiter',
    'all',
    'anext',
    'any',
    'ascii',
    'bin',
    'bool',
    'breakpoint',
    'callable',
    'chr',
    'classmethod',
    'compile',
    'copyright',
    'credits',
    'delattr',
    'dir',
    'eval',
    #'exec',
    'exit',
    'filter',
    'format',
    'globals',
    #'hasattr',
    'hash',
    'help',
    'hex',
    #'id',
    'input',
    #'isinstance',
    'issubclass',
    'license',
    'locals',
    #'map',
    #'max',
    'min',
    'next',
    'oct',
    'open',
    'ord',
    'print',
    'property',
    'quit',
    'staticmethod',
    'sum',
    'super',
    # 'type',
    'vars',
    'zip',
]


def decorate_builtins(decorator):
    for obj_name in builtin_methods:
        obj = getattr(builtins, obj_name)

        if callable(obj):
            create_patch(builtins, None, obj_name, decorator(obj, 'builtins', obj_name))


def decorate_defaults(decorator):
    ignored_methods = get_ignored_methods()
    for module, classes in py_objects.items():
        for class_ in classes:
            for n in dir(class_) + ['comparison']:
                if (class_, n) == (dict, '__iter__'):
                    continue

                if n in ignored_methods:
                    continue

                if is_py_method_def(module, class_, n):
                    orig_method = getattr(class_, n)
                else:
                    orig_method = get_c_method(class_, n)

                if orig_method is None:
                    continue
                    raise Exception(
                        f'Unknwn method {n} of class {class_.__name__} in module {module.__name__}'
                    )

                create_patch(
                    module,
                    class_.__name__,
                    n,
                    decorator(orig_method, class_.__name__, n),
                )


def decorate_all_methods_in_module(module, decorator):
    for name, obj in inspect.getmembers(module):

        # inspect.isfunction only works for user define functions
        # therefore we use callable(obj)
        if callable(obj):
            create_patch(module, None, name, decorator(obj, obj.__name__, name))

        if inspect.isclass(obj) and obj.__name__ != 'BuiltinImporter':
            for name, fn in inspect.getmembers(obj, predicate=inspect.isfunction):
                if name != '__class_getitem__':
                    create_patch(
                        module,
                        obj.__name__,
                        name,
                        decorator(fn, obj.__name__, name),
                    )


def wrap_import(decorator):
    import_wrapper = patch_imports.wrap_it('__import__', patch_imports.wrap_import)
    setattr(builtins, '__import__', decorator(import_wrapper, 'builtins', '__import__'))


def patch_imported_methods(imported_callables, decorator):
    for call in imported_callables:

        if inspect.isclass(call):
            for method_name in dir(call):
                method = getattr(call, method_name, None)
                if callable(method) and method_name != '__class__':
                    create_patch(
                        get_module_by_name(call.__module__),
                        call.__name__,
                        method_name,
                        decorator(method, call.__name__, method_name),
                    )
        else:
            create_patch(
                get_module_by_name(call.__module__),
                None,
                call.__name__,
                decorator(call, None, call.__name__),
            )


def setup_recording(module, ignored_modules: set):
    ignored_modules.add('collections')
    module_imports, imported_callables = get_imports(module)

    imported_callables = [
        cal for cal in imported_callables if cal.__module__ not in ignored_modules
    ]
    module_imports = [
        import_ for import_ in module_imports if import_.__name__ not in ignored_modules
    ]
    user_defined_modules = [
        import_ for import_ in module_imports if is_user_defined_module(import_)
    ] + [module]

    decorator, recorder = decorators.create_decorator_detail(user_defined_modules)

    wrap_import(decorator)

    patch_imported_methods(imported_callables, decorator)

    for module in module_imports:
        decorate_all_methods_in_module(module, decorator)

    decorate_defaults(decorator)

    decorate_builtins(decorator)

    return recorder, user_defined_modules


class recording_activated:
    def __enter__(self):
        apply()

    def __exit__(self, type, value, traceback):
        revert()
