from .builtins_evaluations import builtins_complexities
from .bytes_evaluations import bytes_complexities
from .complex_evaluations import complex_complexities
from .dict_evaluations import dict_complexities
from .float_evaluations import float_complexities
from .int_evaluations import int_complexities
from .list_evaluations import list_complexities
from .set_evaluations import set_complexities
from .str_evaluations import str_complexities


def default_evaluation(_):
    return 1


# TODO fill in complexities for other types
evaluation_method = {
    'builtins': builtins_complexities,
    'bytes': bytes_complexities,
    'complex': complex_complexities,
    'dict': dict_complexities,
    'float': float_complexities,
    'int': int_complexities,
    'list': list_complexities,
    'set': set_complexities,
    'str': str_complexities,
}


def get_evaluation_method(cls_name, func_name):
    return evaluation_method.get(cls_name, {}).get(func_name, default_evaluation)


def evaluate_record(cls, func_name, args):
    if func_name == '__import__':
        return 1
    py_args = []
    for arg in tuple.__iter__(args):
        py_args.append(arg)

    return get_evaluation_method(cls, func_name)(args)
