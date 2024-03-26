def make_generator():
    yield None


async def make_async():
    pass


class EmptyClass:
    pass


class_type = type(EmptyClass)
dict_keys_type = type({}.keys())
dict_items_type = type({}.items())
dict_values_type = type({}.values())
generator_type = type(make_generator())

bytes_iter_type = type(iter(bytes()))
bytearray_iter_type = type(iter(bytearray()))
list_iter_type = type(iter(list()))
dict_iter_type = type(iter(dict()))
set_iter_type = type(iter(set()))
tuple_iter_type = type(iter(tuple()))


non_builtin_types = {
    'class': class_type,
    'dict_keys': dict_keys_type,
    'dict_items': dict_items_type,
    'dict_values': dict_values_type,
    'generator': generator_type,
    'bytes_iter': bytes_iter_type,
    'bytearray_iter': bytearray_iter_type,
    'list_iterator': list_iter_type,
    'dict_keyiterator': dict_iter_type,
    'bytes_iter': bytes_iter_type,
    'set_iter': set_iter_type,
    'tuple_iterator': tuple_iter_type,
}
