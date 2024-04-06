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

from .ignor import ignored_methods
from .patch.patch_imports import import_decorator
from .patch import py_object as pyo
from .patch.default_classes.default_classes import is_py_method_def
from .patch.patching import (
    create_patch,
    apply,
    revert,
)

from .utils.module import (
    get_module_imports,
    get_imports,
    get_module_imports,
    is_user_defined_module,
    get_module_by_name,
)
from .utils.utils import get_c_method

from .ignor import (
    get_def_ignored_modules,
    ignored_specifics,
    ignored_classes,
    ignored_class_methods,
)

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
    # 'bool',
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
    for module, classes in py_objects.items():
        for class_ in classes:
            for n in dir(class_) + ['comparison']:
                if n in ignored_methods or (class_, n) in ignored_specifics:
                    continue

                if is_py_method_def(module, class_, n):
                    orig_method = getattr(class_, n)
                else:
                    orig_method = get_c_method(class_, n)

                if orig_method is None:
                    raise Exception(
                        f'Unknown method {n} of class {class_.__name__} in module {module.__name__}'
                    )

                create_patch(
                    module,
                    class_.__name__,
                    n,
                    decorator(orig_method, class_.__name__, n),
                )


def decorate_all_methods_in_module(module, decorator):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            if obj.__name__ in ignored_classes:
                continue

            for name, fn in inspect.getmembers(obj, predicate=inspect.isfunction):
                if name not in ignored_class_methods:
                    create_patch(
                        module,
                        obj.__name__,
                        name,
                        decorator(fn, obj.__name__, name),
                    )
        # inspect.isfunction only works for user define functions
        # therefore we use callable(obj)
        elif callable(obj):
            create_patch(module, None, name, decorator(obj, module.__name__, name))


def wrap_import(decorator, user_defined_modules):
    import_wrapper = import_decorator(decorator, user_defined_modules)

    create_patch(
        builtins,
        None,
        '__import__',
        decorator(import_wrapper, 'builtins', '__import__'),
    )


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
    setup_modules, setup_callables = get_def_ignored_modules()
    ignored_modules.update(setup_modules)
    module_imports, imported_callables = get_module_imports(module, ignored_modules)

    imported_callables = [
        cal
        for cal in imported_callables
        if get_module_by_name(cal.__module__) not in ignored_modules
        and cal not in setup_callables
    ]
    module_imports = [
        import_ for import_ in module_imports if import_ not in ignored_modules
    ]
    user_defined_modules = [
        import_ for import_ in module_imports if is_user_defined_module(import_)
    ] + [module]

    decorator, recorder = decorators.create_decorator_detail(user_defined_modules)

    wrap_import(decorator, user_defined_modules)

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
