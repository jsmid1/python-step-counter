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

non_builtin_types = {
    'class': class_type,
    'dict_keys': dict_keys_type,
    'dict_items': dict_items_type,
    'dict_values': dict_values_type,
    'generator': generator_type,
}
