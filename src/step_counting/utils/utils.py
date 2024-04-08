import inspect
import ctypes
from sys import stdlib_module_names

from ..patch import py_object as pyo


def is_std_module(module):
    parent_module = module.__name__.split('.')[0]

    return parent_module in stdlib_module_names


def get_class_methods(cls):
    members = inspect.getmembers(cls)

    methods = [
        member for member in members if inspect.isroutine(getattr(cls, member[0]))
    ]

    return [method_name for (method_name, _) in methods]


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
