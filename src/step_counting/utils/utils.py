import inspect
import ctypes
from ..patch import py_object as pyo


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
