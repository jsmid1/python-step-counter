import builtins
from ..original_methods import (
    _getattr,
    _setattr,
    _hasattr,
    _import,
    _isinstance,
    _type,
    dict_get,
)


replacement_import_methods = {}


class module_proxy:
    pass


def make_proxy(module):
    proxy = module_proxy()
    proxy.__name__ = module.__name__

    replacement_methods = replacement_import_methods.get(module.__name__, None)

    if replacement_methods is None:
        return module

    for (class_name, method_name), replacement_method in replacement_methods.items():
        if replacement_method is None:
            continue

        if class_name is not None:
            if not _hasattr(module, class_name):
                raise Exception(
                    f'Module {module.__name__} does not contain method {method_name}'
                )

            if _hasattr(proxy, class_name):
                class_ = _getattr(proxy, class_name)
            else:
                class_ = _getattr(module, class_name)

            _setattr(class_, method_name, replacement_method)
            _setattr(proxy, class_name, class_)
        else:
            if not _hasattr(module, method_name):
                raise Exception(
                    f'Class {class_name} in module {module.__name__} does not contain method {method_name}'
                )

            _setattr(proxy, method_name, replacement_method)

    return proxy


def wrap_import(_, old, name, *args, **kwargs):
    if dict_get(replacement_import_methods, name, None) is not None:
        return make_proxy(_import(name, *args, **kwargs))

    return old(name, *args, **kwargs)


def wrap_it(attr, func):
    old = _getattr(builtins, attr)

    def with_patched(*args, **kwargs):
        return func(attr, old, *tuple.__iter__(args), **kwargs)

    patched = func if _isinstance(func, _type) else with_patched

    return patched
