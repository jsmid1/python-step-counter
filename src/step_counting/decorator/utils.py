import sys
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


def get_caller_module_info():
    try:
        caller_frame = sys._getframe(2)
    except:
        return None, 0

    module_name = dict_get(caller_frame.f_globals, '__name__', None)
    line_number = caller_frame.f_lineno

    return module_name, line_number
