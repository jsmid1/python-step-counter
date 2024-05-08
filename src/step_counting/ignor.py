from importlib.machinery import BuiltinImporter, FrozenImporter
from typing import Hashable, Optional

ignored_object_methods = {
    '__class__',
    '__dir__',
    '__getattribute__',
    '__init__',
    '__new__',
    '__next__',
    '__doc__',
    '__delitem__',  # Performed by the same function as setitem
    '__alloc__',
    '__format__',  # Can be removed after fix in restrict
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

ignored_win_methods = {
    '_LCMapStringEx',
    '_nt_readlink',
}

ignored_methods = set.union(
    ignored_object_methods,
    comparison_operations,
    ignored_r_methods,
    ignored_win_methods,
)

ignored_specifics = {
    (dict, '__iter__'),
}

ignored_classes = {BuiltinImporter, FrozenImporter}


def is_ignored(class_: Optional[type], method_name: Optional[str]) -> bool:
    """
    Checks if either class_, method_name or their combination are ignored.

    Parameters
    ----------
    class_ (Optional[type]): class
    method_name (str): name of the method

    Returns
    -------
    bool: Infromation if the class_ or method are ignored.
    """
    return (
        (
            class_
            and (
                class_ in ignored_classes
                or not issubclass(class_, Hashable)
                and method_name == '__hash__'
            )
        )
        or method_name in ignored_methods
        or (class_, method_name) in ignored_specifics
    )
