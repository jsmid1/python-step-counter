import types
import inspect
import os
import sys


def get_module_by_name(module_name):
    try:
        return sys.modules[module_name]
    except:
        raise Exception(f'Unkown module: module_name')


def is_user_defined_module(module):
    # To check if the module is defined bu the user
    # try to get the module's file path
    # if the module is builtin, inspect.getfile will raise a TypeError
    try:
        module_file = inspect.getfile(module)
    except TypeError:
        return False

    std_lib_path = os.path.dirname(os.__file__)
    site_packages_paths = [
        site_package_path
        for site_package_path in sys.path
        if 'site-packages' in site_package_path
    ]

    if module_file.startswith(std_lib_path) or any(
        module_file.startswith(path) for path in site_packages_paths
    ):
        return False
    else:
        return True


def get_imports(mod):
    imported_modules = set()
    imported_functions = set()
    for name, obj in vars(mod).items():
        if isinstance(obj, types.ModuleType):
            # if inspect.ismodule(obj) or type(obj).__name__ == 'module_proxy':
            imported_modules.add(obj)
        elif (
            callable(obj)
            and hasattr(obj, '__module__')
            and obj.__module__ != mod.__name__
        ):
            if callable(obj):
                imported_functions.add(obj)

    subimports = set()
    for module in imported_modules:
        if is_user_defined_module(module):
            imps, funcs = get_imports(module)
            subimports.update(imps)
            imported_functions.update(funcs)

    imported_modules.update(subimports)

    return imported_modules, imported_functions


def get_module_imports(mod, ignored_modules):
    if mod in ignored_modules:
        return {}, {}

    imported_modules = set()
    imported_functions = set()
    for name, obj in vars(mod).items():
        if isinstance(obj, types.ModuleType):
            # if inspect.ismodule(obj) or type(obj).__name__ == 'module_proxy':
            imported_modules.add(obj)
        elif (
            callable(obj)
            and hasattr(obj, '__module__')
            and obj.__module__ != mod.__name__
        ):
            if callable(obj):
                imported_functions.add(obj)

    subimports = set()
    for module in imported_modules:
        if is_user_defined_module(module):
            imps, funcs = get_module_imports(module, ignored_modules)
            subimports.update(imps)
            imported_functions.update(funcs)

    imported_modules.update(subimports)

    return imported_modules, imported_functions
