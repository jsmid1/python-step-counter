import functools

import inspect
import sys

str_startswith = str.startswith
dict_get = dict.get


set_new = set
set_intersection = set.intersection
list_contains = list.__contains__
_print = print

import sys
from .records import record_classes
from ..utils import utils

str_eq = str.__eq__
list_iter = list.__iter__

_print = print
str_find = str.find
str_startswith = str.startswith
list_index = list.index
dict_getitem = dict.__getitem__
dict_get = dict.get
int_eq = int.__eq__

set_add = set.add


# TODO make something better. this is abomination
def str_in_list(string, lst):
    # keys_dict = {str(item): True for item in list_iter(lst)}
    # try:
    #     return dict_getitem(keys_dict, str(string))
    # except KeyError:
    #     return False

    # TODO check, possible hash collisions
    # theoratically incorect
    for item in list_iter(lst):
        if int_eq(hash(item), hash(string)):
            return True
    return False


def create_decorator_default(tracked_modules):
    records = record_classes.simple_call_recorder()

    def decorator(func, klass, func_name):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            module_name, _ = utils.get_caller_module_info()
            # if list_contains(tracked_modules, module_name):
            records.add_record(klass, func_name, args)
            return func(*args, **kwargs)

        return wrapper

    return decorator, records


def create_custom_decorator(
    recorder: record_classes.simple_call_recorder, allowed_modules
):
    def decorator(func, target_class, orig_func_name):
        @functools.wraps(target_class, orig_func_name)
        def wrapper(*args, **kwargs):
            recorder.add_record(target_class, orig_func_name, args)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def create_decorator_detail(tracked_modules):
    recorder = record_classes.detail_call_recorder()

    def decorator(func, klass, func_name):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            module_name, line_number = utils.get_caller_module_info()
            if str_in_list(module_name, tracked_modules):

                recorder.add_record(module_name, line_number, klass, func_name, args)

            return func(*args, **kwargs)

        return wrapper

    return decorator, recorder
