import builtins
import inspect
import traceback
from types import ModuleType
from typing import Any, Callable, Optional

from src.step_counting.decorator.records.record_classes import DetailCallRecorder
from .ib111_restrictions import default_types, builtin_methods, ib111_imports
from .decorator.decorators import create_decorator_detail, Decorator

from .ignor import ignored_methods, ignored_object_methods
from .patch.patch_imports import import_decorator
from .patch.default_classes.default_classes import is_py_method_def
from .patch.patching import (
    create_patch,
    apply,
    revert,
)
from .utils.module import (
    get_module_imports,
    is_user_defined_module,
    get_module_by_name,
)
from .utils.methods import get_c_method

from .ignor import (
    get_def_ignored_modules,
    ignored_specifics,
    ignored_classes,
    ignored_class_methods,
)


def decorate_builtins(decorator: Decorator) -> None:
    for obj_name in builtin_methods:
        obj = getattr(builtins, obj_name)

        if callable(obj):
            create_patch(
                builtins, None, obj_name, decorator(builtins, None, obj, obj_name)
            )


def decorate_defaults(decorator: Decorator) -> None:
    for module, classes in default_types.items():
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

                if callable(orig_method):
                    create_patch(
                        module,
                        class_.__name__,
                        n,
                        decorator(module, class_, orig_method, n),
                    )


def decorate_class(
    module: ModuleType, class_: type, predicate, decorator: Decorator
) -> None:
    for name, fn in inspect.getmembers(class_, predicate=predicate):
        if name not in ignored_class_methods and name not in ignored_object_methods:
            create_patch(
                module,
                class_.__name__,
                name,
                decorator(module, class_, fn, name),
            )


def decorate_all_methods_in_module(module: ModuleType, decorator: Decorator) -> None:
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            if obj.__name__ in ignored_classes:
                continue

            decorate_class(module, obj, inspect.isfunction, decorator)

        elif inspect.isroutine(obj):
            create_patch(
                module,
                None,
                name,
                decorator(get_module_by_name(obj.__module__), None, obj, name),
            )


def decorate_ib111_modules(decorator: Decorator) -> None:
    for module, object_names in ib111_imports.items():
        for obj_name in object_names:
            obj = getattr(module, obj_name)
            if inspect.ismodule(obj):
                decorate_all_methods_in_module(obj, decorator)
            if inspect.isclass(obj):
                decorate_class(module, obj, inspect.isroutine, decorator)
                # for method_name in get_class_methods(obj):
                #     if method_name in ignored_object_methods:
                #         continue

                #     method = getattr(obj, method_name)
                #     create_patch(
                #         module,
                #         obj_name,
                #         method_name,
                #         decorator(module, obj, method, method_name),
                #     )
            elif inspect.isroutine(obj):
                create_patch(
                    module, None, obj_name, decorator(module, None, obj, obj_name)
                )


def wrap_import(decorator: Decorator, user_defined_modules: set[ModuleType]) -> None:
    import_wrapper = import_decorator(decorator, user_defined_modules)

    create_patch(
        builtins,
        None,
        '__import__',
        decorator(builtins, None, import_wrapper, '__import__'),
    )


def patch_imported_methods(
    imported_callables: set[Callable[..., Any]], decorator: Decorator
) -> None:
    for call in imported_callables:
        module = get_module_by_name(call.__module__)
        if inspect.isclass(call):
            if call in default_types.values() or call in ib111_imports.values():
                continue
            decorate_class(module, call, inspect.isroutine, decorator)
        else:
            create_patch(
                module,
                None,
                call.__name__,
                decorator(module, None, call, call.__name__),
            )


def setup_recording(
    module: ModuleType, ignored_modules: set[ModuleType]
) -> tuple[DetailCallRecorder, set[ModuleType]]:
    setup_modules, _ = get_def_ignored_modules()
    ignored_modules.update(setup_modules)
    module_imports, imported_callables = get_module_imports(module, ignored_modules)

    imported_user_callables = {
        cal
        for cal in imported_callables
        if is_user_defined_module(get_module_by_name(cal.__module__))
    }

    user_defined_modules = {
        import_
        for import_ in module_imports
        if is_user_defined_module(import_) and import_ not in ignored_modules
    }
    user_defined_modules.add(module)

    decorator, recorder = create_decorator_detail(user_defined_modules)

    wrap_import(decorator, user_defined_modules)

    patch_imported_methods(imported_user_callables, decorator)
    for module in user_defined_modules:
        decorate_all_methods_in_module(module, decorator)

    decorate_defaults(decorator)
    decorate_builtins(decorator)
    decorate_ib111_modules(decorator)

    return recorder, user_defined_modules


class RecodingActivated:
    def __enter__(self) -> None:
        apply()

    def __exit__(
        self,
        type: Optional[BaseException],
        value: Optional[BaseException],
        traceback: Optional[traceback.TracebackException],
    ) -> None:
        revert()
