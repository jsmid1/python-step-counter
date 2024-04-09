from ast import FunctionType
import ctypes
import gc
import inspect
from types import ModuleType
from typing import Any, Callable, Optional

from ..utils.module import is_user_defined_module
from . import py_object as pyo
from ..non_builtin_types import non_builtin_types
from .default_classes.default_classes import is_py_method_def
from .bin import patchdictionary, patchint, patchtuple, patchstr, patchlist  # type: ignore
from .method_switch import MethodSwitch
from ..utils.methods import get_c_method, get_class_methods
from ..utils.module import is_std_module

tp_func_dict = {}


def substitute_py_methods_structure(
    tyobj: pyo.PyTypeObject,
    tp_name: str,
    struct_ty: type[ctypes.Structure],
) -> None:
    tp_as_obj = struct_ty()
    tp_as_new_ptr = ctypes.cast(ctypes.addressof(tp_as_obj), ctypes.POINTER(struct_ty))

    setattr(tyobj, tp_name, tp_as_new_ptr)


def patch_py_object_method_with_type(
    class_: Optional[type],
    tp_name: str,
    method_name: Optional[str],
    method_type: Any,
    replacement_method: Any,
) -> None:
    tyobj = pyo.PyTypeObject.from_address(id(class_))

    if inspect.isfunction(replacement_method):
        cfunc = method_type(replacement_method)
    else:
        cfunc = ctypes.cast(replacement_method, method_type)

    if tp_name in dict.__iter__(pyo.py_type_object_structs):
        struct_ty = pyo.py_type_object_structs[tp_name]
        tp_as_ptr = getattr(tyobj, tp_name)
        if not tp_as_ptr:
            substitute_py_methods_structure(tyobj, tp_name, struct_ty)

        tp_as = tp_as_ptr[0]
        tp_func_dict[(class_, tp_name, method_name)] = cfunc

        assert method_name
        setattr(tp_as, method_name, cfunc)
    else:
        tp_func_dict[(class_, tp_name, None)] = cfunc

        # override function call
        setattr(tyobj, tp_name, cfunc)


def patch_py_object_method(
    module: ModuleType,
    class_: Optional[type],
    method_name: str,
    replacement_method: Callable[..., Any],
) -> None:
    assert class_
    spec_method = special_patch_methods.get(class_.__name__, {}).get(method_name, None)
    if spec_method is not None:
        spec_method(replacement_method)
        return

    method_info = pyo.get_function_mapping(class_, method_name)
    if method_info is None:
        raise Exception(
            f'Function {method_name} is not defined in builtins in {class_}!'
        )

    c_structure, c_name, type_ = method_info
    c_type = ctypes.CFUNCTYPE(*type_)
    patch_py_object_method_with_type(
        class_, c_structure, c_name, c_type, replacement_method
    )


def patch_py_builtin_method(
    module: ModuleType,
    class_: Optional[type],
    method_name: str,
    replacement_method: Callable[..., Any],
) -> None:
    setattr(module, method_name, replacement_method)


def patchable_builtin(class_: type) -> Any:
    refs = gc.get_referents(class_.__dict__)
    assert len(refs) == 1
    return refs[0]


def get_py_std_class_method(class_: type, method_name: str) -> Any:
    dikt = patchable_builtin(class_)

    return dikt.get(method_name, None)


def patch_py_std_class_method(
    module: ModuleType,
    class_: Optional[type],
    method_name: str,
    replacement_method: Callable[..., Any],
) -> None:
    assert class_
    dikt = patchable_builtin(class_)

    try:
        dikt[method_name] = replacement_method
    except Exception:
        raise Exception(f"Unknown method {method_name} of class {class_.__name__}")

    ctypes.pythonapi.PyType_Modified(ctypes.py_object(class_))


def patch_user_defined_method(
    module: ModuleType,
    class_: Optional[type],
    method_name: str,
    replacement_method: Callable[..., Any],
) -> None:
    if class_ is None:
        setattr(module, method_name, replacement_method)
    else:
        if method_name not in get_class_methods(class_):
            raise Exception(
                f'Class {class_.__name__} in module {module.__name__} does not contain method {method_name}!'
            )
        setattr(class_, method_name, replacement_method)


# TODO: Check which are actually necessary
special_patch_methods = {
    'int': {
        'comparison': patchint.patch_int_richcompare,
    },
    'tuple': {
        '__len__': patchtuple.patch_tuple_len,
        '__getitem__': patchtuple.patch_tuple_getitem,
    },
    'tuple_iterator': {
        '__next__': patchtuple.patch_tuple_iterator_next,
    },
    'dict': {
        '__getitem__': patchdictionary.patch_dictionary_getitem,
        #'__setitem__': patchdictionary.patch_dictionary_setitem,
        #'__contains__': patchdictionary.patch_dictionary_contains,
        '__iter__': patchdictionary.patch_dictionary_iter,
    },
    'list': {
        '__getitem__': patchlist.patch_list_getitem,
    },
    'str': {
        '__getitem__': patchstr.patch_str_getitem,
    },
}


def patch_with_module(
    class_: str, method_name: str, replacement_method: Callable[..., Any]
) -> None:
    special_patch_methods[class_][method_name](replacement_method)


method_switches: dict[tuple[ModuleType, Optional[type], str], MethodSwitch] = dict()


def create_patch(
    module: ModuleType,
    class_: Optional[str],
    method_name: str,
    replacement_method: Callable[..., Any],
) -> None:
    if is_std_module(module):
        if class_ is None:
            patching_method = patch_py_builtin_method
            original_method = getattr(module, method_name)
            class_to_patch = None
        else:
            class_to_patch = non_builtin_types.get(class_, None)

            if class_to_patch is None:
                class_to_patch = getattr(module, class_)

            if class_to_patch is None:
                raise Exception(f'Given class: {class_} is not defined in builtins!')

            if (
                module.__name__ in {'builtins', 'collections'}
                and pyo.get_function_mapping(class_to_patch, method_name) is not None
            ):
                patching_method = patch_py_object_method
                original_method = get_c_method(class_to_patch, method_name)
            else:
                patching_method = patch_py_std_class_method
                original_method = get_py_std_class_method(class_to_patch, method_name)

    elif is_user_defined_module(module):
        if class_ == None:
            original_method = getattr(module, method_name)
            class_to_patch = None
        else:
            assert class_
            class_to_patch = getattr(module, class_)
            original_method = getattr(class_to_patch, method_name)
        patching_method = patch_user_defined_method

    else:
        raise Exception(
            f'Unknown method {method_name} of class {class_} in module {module.__name__}'
        )

    global method_switches
    method_identification = (module, class_to_patch, method_name)
    if method_identification in method_switches:
        method_switches[method_identification].set_replacement_method(
            replacement_method
        )
    else:
        method_switches[(module, class_to_patch, method_name)] = MethodSwitch(
            patching_method,
            original_method,
            replacement_method,
        )


def apply_one(module: ModuleType, class_: Optional[type], method_name: str) -> None:
    ms = method_switches.get((module, class_, method_name))
    if ms is None:
        raise Exception(
            f'{module.__name__}, {class_}, {method_name} is not a valid patch'
        )
    assert ms
    ms.overwrite(module, class_, method_name, ms.get_replacement_method())


def revert_one(module: ModuleType, class_: Optional[type], method_name: str) -> None:
    ms = method_switches.get((module, class_, method_name))
    if ms is None:
        raise Exception(
            f'{module.__name__}, {class_}, {method_name} is not a valid patch'
        )
    assert ms
    ms.overwrite(module, class_, method_name, ms.get_original_method())


def apply() -> None:
    for (module, class_, method_name), ms in method_switches.items():
        ms.overwrite(module, class_, method_name, ms.get_replacement_method())


def revert() -> None:
    for (module, class_, method_name), ms in method_switches.items():
        ms.overwrite(module, class_, method_name, ms.get_original_method())
