ignored_object_methods = {
    '__class__',
    '__dir__',
    '__getattribute__',
    '__hash__',
    '__init__',
    '__new__',
    '__delattr__',
    '__doc__',
    '__getnewargs__',
    '__init_subclass__',
    '__reduce__',
    '__reduce_ex__',
    '__sizeof__',
    '__subclasshook__',
    '__delitem__',
    '__alloc__',
    '__setformat__',
}

comparison_operations = {'__eq__', '__ge__', '__gt__', '__le__', '__lt__', '__ne__'}

ignored_r_methods = {
    '__radd__',
    '__rand__',
    '__rdivmod__',
    '__rfloordiv__',
    '__rlshift__',
    '__rmod__',
    '__rmul__',
    '__ror__',
    '__rpow__',
    '__rrshift__',
    '__rsub__',
    '__rtruediv__',
    '__rxor__',
}


def get_ignored_methods():
    return set.union(ignored_object_methods, comparison_operations, ignored_r_methods)
