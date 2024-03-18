_setattr = setattr
_getattr = getattr
_hasattr = hasattr

_isinstance = isinstance
_tuple_iter = tuple.__iter__

_type = type


replacement_import_methods = {}


class module_proxy:
    pass


def make_proxy(module):
    proxy = module_proxy()
    proxy.__name__ = module.__name__

    replacement_methods = replacement_import_methods.get(module.__name__, None)

    if replacement_methods is None:
        return module

    for method_name, replacement_method in replacement_methods.items():

        if not _hasattr(module, method_name):
            raise Exception(
                f'Module {module.__name__} does not contain method {method_name}'
            )

        if replacement_method is not None:
            _setattr(proxy, method_name, replacement_method)

    return proxy


str.lower
import builtins

builtins_import = builtins.__import__


def wrap_import(func_name, old, name, *args, **kwargs):

    if name in replacement_import_methods:
        return make_proxy(builtins_import(name, *args, **kwargs))

    return old(name, *args, **kwargs)


import builtins


def wrap_it(klass, attr, func):
    old = _getattr(builtins, attr)

    def with_patched(*args, **kwargs):
        return func(attr, old, *_tuple_iter(args), **kwargs)

    patched = func if _isinstance(func, _type) else with_patched

    return patched
