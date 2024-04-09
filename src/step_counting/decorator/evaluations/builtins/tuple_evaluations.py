from ..complexities import constant, linear_to_len


tuple_complexities = {
    '__len__': constant,
    '__getitem__': constant,
    '__contains__': linear_to_len,
    '__iter__': constant,
    'count': linear_to_len,
    'index': linear_to_len,
}
