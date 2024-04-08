import inspect

from ..utils.module import is_user_defined_module
from ..original_methods import _setattr, _import, _callable

########################################################################################
# These methods are used with patches applied. Even though it is not necessary
# to use original methods, they are used for optimalization.
########################################################################################


class module_proxy:
    pass


class class_proxy:
    pass


def make_proxy(module, decorator):
    proxy = module_proxy()
    proxy.__name__ = module.__name__

    for name, obj in module.__dict__.items():
        if inspect.isclass(obj):
            class_ = class_proxy()
            for attr_name in dir(obj):
                if attr_name == '__class__':
                    continue

                attr = getattr(obj, attr_name)
                if _callable(attr):
                    _setattr(class_, attr_name, decorator(attr, obj, attr_name))
            _setattr(proxy, name, class_)
        elif _callable(obj):
            if hasattr(obj, '__module__') and obj.__module__ == module.__name__:
                _setattr(proxy, name, decorator(obj, module, obj.__name__))

    return proxy


def import_proxy(decorator, user_defined_modules, name, *args, **kwargs):
    module = _import(name, *args, **kwargs)
    if is_user_defined_module(module):
        user_defined_modules.append(module)
        return make_proxy(module, decorator)
    return module


def import_decorator(decorator, user_defined_modules):
    def wrapped_import(*args, **kwargs):
        return import_proxy(
            decorator, user_defined_modules, *tuple.__iter__(args), **kwargs
        )

    return wrapped_import
