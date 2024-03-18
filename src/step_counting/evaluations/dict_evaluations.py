from .complexities import constant, linear_to_len


def dict_update_complexity(args):
    list_one = args[0]
    list_two = args[1]
    return len(list_one) + len(list_two)


# TODO possible problems due to hash collisions...
dict_complexities = {
    '__contains__': linear_to_len,
    '__len__': constant,
    '__getitem__': constant,
    '__iter__': linear_to_len,
    '__setitem__': constant,
    'clear': linear_to_len,
    'copy': linear_to_len,
    'fromkeys': linear_to_len,
    'get': constant,
    'items': constant,  # TODO check, view object creation
    'keys': constant,  # TODO ^
    'pop': constant,
    'popitem': constant,
    'setdefault': constant,
    'update': dict_update_complexity,
    'values': constant,  # TODO check, view object creation
}
