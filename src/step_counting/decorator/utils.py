import sys
import types

from ..original_methods import list_iter, int_eq, dict_get

_hash = hash


# TODO make something better. this is abomination
def obj_in_list(string, lst):
    # keys_dict = {str(item): True for item in list_iter(lst)}
    # try:
    #     return dict_getitem(keys_dict, str(string))
    # except KeyError:
    #     return False

    # TODO check, possible hash collisions
    # theoratically incorect
    for item in list_iter(lst):
        # print(hash(item), hash(string))
        if int_eq(_hash(item.__name__), _hash(string)):
            return True
    return False


Py_LT, Py_LE, Py_EQ, Py_NE, Py_GT, Py_GE = range(6)
comparison_methods = {
    Py_LT: '__lt__',
    Py_LE: '__le__',
    Py_EQ: '__eq__',
    Py_NE: '__ne__',
    Py_GT: '__gt__',
    Py_GE: '__ge__',
}
_isinstance = isinstance


def get_method_type(cls, method_name):
    if method_name == 'comparison':
        return types.FunctionType

    if hasattr(cls, '__dict__') and method_name in cls.__dict__:
        method = cls.__dict__[method_name]
        if _isinstance(method, staticmethod):
            return staticmethod
        elif _isinstance(method, classmethod):
            return classmethod

    method = getattr(cls, method_name, None)
    if method:
        if _isinstance(method, (types.BuiltinFunctionType, types.MethodType)):
            return staticmethod
        elif callable(method):
            return types.FunctionType

    raise ValueError(f'Method {method_name} not found in {cls}.')


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

    return module_name, line_number
