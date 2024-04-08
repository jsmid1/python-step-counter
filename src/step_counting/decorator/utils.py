import sys
import types

from ..original_methods import _hash, dict_get

Py_LT, Py_LE, Py_EQ, Py_NE, Py_GT, Py_GE = range(6)
comparison_methods = {
    Py_LT: '__lt__',
    Py_LE: '__le__',
    Py_EQ: '__eq__',
    Py_NE: '__ne__',
    Py_GT: '__gt__',
    Py_GE: '__ge__',
}

########################################################################################
# These method are used with patches aplied. Therefore use of regular methods is
# severly limited.
# To avoid unwanted recursion it is necessary to use methods that have not been
# decorated by this decorator.
########################################################################################


def module_in_list(module, lst):
    for item in list.__iter__(lst):
        if int.__eq__(_hash(module), _hash(item)):
            return True
    return False


def determine_method(method_name, args):
    if str.__eq__(method_name, 'comparison'):
        return dict.__getitem__(comparison_methods, tuple.__getitem__(args, 2))

    return method_name


def get_caller_module_info():
    try:
        caller_frame = sys._getframe(2)
    except:
        return None, 0

    module_name = dict_get(caller_frame.f_globals, '__name__', None)
    line_number = caller_frame.f_lineno

    module = dict_get(sys.modules, module_name, None)

    return module, line_number


########################################################################################


def get_method_type(cls, method_name):
    if method_name == 'comparison':
        return types.FunctionType

    if hasattr(cls, '__dict__') and method_name in cls.__dict__:
        method = cls.__dict__[method_name]
        if isinstance(method, staticmethod):
            return staticmethod
        elif isinstance(method, classmethod):
            return classmethod

    method = getattr(cls, method_name, None)
    if method:
        if isinstance(method, (types.BuiltinFunctionType, types.MethodType)):
            return staticmethod
        elif callable(method):
            return types.FunctionType

    raise ValueError(f'Method {method_name} not found in {cls}.')
