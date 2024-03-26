import ast
import os
import sys

import sys
import os
import inspect


def get_class_methods(cls):
    method_names = []
    for attr_name in dir(cls):
        attr = None
        if hasattr(cls, attr_name):
            attr = getattr(cls, attr_name)
        if callable(attr):
            if inspect.ismethod(attr) or inspect.isfunction(attr):
                method_names.append(attr_name)
    return method_names


def is_user_defined_module(module):
    # Get the module's file path
    try:
        module_file = inspect.getfile(module)
    except TypeError:
        # If the module is builtin, inspect.getfile will raise a TypeError
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


def get_full_module_name(module):
    if module.__package__:
        return f'{module.__package__}.{module.__name__}'
    else:
        return module.__name__


def get_module_object(module_name):
    return sys.modules.get(module_name, None)
    # try:
    #     return sys.modules.get(module_name, None)
    # except KeyError:
    #     __import__(module_name)
    #     return sys.modules.get(module_name, None)


def get_module_file_path(module):
    try:
        return module.__file__
    except AttributeError:
        return None  # builtin module case


def get_module_imports(module_name, seen_modules=None):
    if seen_modules is None:
        seen_modules = set()

    module = get_module_object(module_name)
    if module is None or module in seen_modules:
        return list(seen_modules)

    seen_modules.add(module)
    module_file = get_module_file_path(module)

    if module_file and module_file.endswith('.py'):
        with open(module_file, 'r') as file:
            node = ast.parse(file.read(), filename=module_file)

        for elem in node.body:
            if isinstance(elem, ast.Import):
                for alias in elem.names:
                    get_module_imports(alias.name, seen_modules)
            elif isinstance(elem, ast.ImportFrom):
                if elem.module:
                    get_module_imports(elem.module, seen_modules)

    return list(seen_modules)


import importlib.util


def get_module_path(module_name):
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        return None
    return spec.origin


dict_get = dict.get
_print = print
int_repr = int.__repr__


def get_caller_module_info():
    try:
        caller_frame = sys._getframe(2)
    except:
        return None, 0

    module_name = dict_get(caller_frame.f_globals, '__name__', None)

    line_number = caller_frame.f_lineno

    # _print(module_name, int_repr(line_number))
    return module_name, line_number


import ctypes
from ..patch import py_object as pyo


def get_c_method(class_, method_name):
    tyobj = pyo.PyTypeObject.from_address(id(class_))

    method_mapping_info = pyo.get_function_mapping(class_, method_name)
    if method_mapping_info is None:
        return None

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
