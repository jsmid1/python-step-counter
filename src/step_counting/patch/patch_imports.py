import inspect
from types import ModuleType
from typing import Any, Callable, Union

from ..utils.module import is_user_defined_module
from ..original_methods import _setattr, _import, _callable

########################################################################################
# These methods are used with patches applied. Even though it is not necessary
# to use original methods, they are used for optimization.
########################################################################################


class ModuleProxy:
    pass


class ClassProxy:
    pass


def make_proxy(module: ModuleType, decorator: Callable[..., Any]) -> ModuleProxy:
    proxy = ModuleProxy()
    _setattr(proxy, '__name__', module.__name__)

    for name, obj in module.__dict__.items():
        if inspect.isclass(obj):
            class_ = ClassProxy()
            for attr_name in dir(obj):
                if attr_name == '__class__':
                    continue

                attr = getattr(obj, attr_name)
                if _callable(attr):
                    _setattr(class_, attr_name, decorator(module, obj, attr, attr_name))
            _setattr(proxy, name, class_)
        elif _callable(obj):
            if hasattr(obj, '__module__') and obj.__module__ == module.__name__:
                _setattr(proxy, name, decorator(module, None, obj, obj.__name__))

    return proxy


def import_proxy(
    decorator: Callable[..., Any],
    user_defined_modules: set[ModuleType],
    name: str,
    *args: Any,
    **kwargs: Any
) -> Union[ModuleType, ModuleProxy]:
    module = _import(name, *args, **kwargs)
    if is_user_defined_module(module):
        user_defined_modules.add(module)
        return make_proxy(module, decorator)
    return module


def import_decorator(
    decorator: Callable[..., Any], user_defined_modules: set[ModuleType]
) -> Callable[..., Union[ModuleType, ModuleProxy]]:
    def wrapped_import(*args: Any, **kwargs: Any) -> Union[ModuleType, ModuleProxy]:
        return import_proxy(
            decorator, user_defined_modules, *tuple.__iter__(args), **kwargs
        )

    return wrapped_import
