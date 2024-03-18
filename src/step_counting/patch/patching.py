import builtins
import ctypes
import gc

from ..utils import utils
from . import patch_imports, method_switch

from . import py_object as pyo
from ..non_builtin_types import non_builtin_types
from .bin import patchdictionary, patchint, patchlist, patchtuple

# from ..original_methods import dict_iter


tp_as_dict = {}
tp_func_dict = {}


def substitute_py_methods_structure(_, class_, tyobj, tp_name, struct_ty):
    tp_as_obj = struct_ty()
    # tp_as_dict[(class_, tp_name)] = tp_as_obj
    tp_as_new_ptr = ctypes.cast(ctypes.addressof(tp_as_obj), ctypes.POINTER(struct_ty))

    setattr(tyobj, tp_name, tp_as_new_ptr)


def patch_py_object_method_with_type(
    class_, tp_name, method_name, method_type, replacement_method
):
    tyobj = pyo.PyTypeObject.from_address(id(class_))

    cfunc = method_type(replacement_method)

    if tp_name in dict.__iter__(pyo.py_type_object_structs):
        struct_ty = pyo.py_type_object_structs[tp_name]
        tp_as_ptr = getattr(tyobj, tp_name)
        if not tp_as_ptr:
            substitute_py_methods_structure(class_, tyobj, tp_name, struct_ty)

        tp_as = tp_as_ptr[0]
        tp_func_dict[(class_, tp_name, method_name)] = cfunc

        setattr(tp_as, method_name, cfunc)
    else:
        if not (class_, tp_name) in tp_as_dict:
            tp_as_dict[(class_, tp_name)] = ctypes.cast(
                getattr(tyobj, tp_name), method_type
            )

        tp_func_dict[(class_, tp_name)] = cfunc

        # override function call
        setattr(tyobj, tp_name, cfunc)


def patch_py_object_method(_, class_, method_name, replacement_method):
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


def patch_py_builtin_method(_, method_name, replacement_method):
    _setattr(builtins, method_name, replacement_method)


def patchable_builtin(class_):
    refs = gc.get_referents(class_.__dict__)
    assert len(refs) == 1
    return refs[0]


def get_py_builtin_class_method(class_, method_name):
    dikt = patchable_builtin(class_)

    return dikt.get(method_name, None)


def patch_py_builtin_class_method(_, class_, method_name, patched_func):
    dikt = patchable_builtin(class_)

    try:
        dikt[method_name] = patched_func
    except Exception:
        raise Exception(f"Unknown method {method_name} of class {class_.__name__}")
    ctypes.pythonapi.PyType_Modified(ctypes.py_object(class_))


def patch_user_defined_method(module, class_: str, method_name, replacement_method):
    if class_ is None:
        setattr(module, method_name, replacement_method)
    else:
        class_to_patch = getattr(module, class_)

        if method_name not in utils.get_class_methods(class_to_patch):
            raise Exception(
                f'Class {class_} in module {module.__name__} does not contain method {method_name}!'
            )
        setattr(class_to_patch, method_name, replacement_method)


# TODO: Check which are actually necessary
special_patch_methods = {
    'int': {
        'comparison': patchint.patch_int_richcompare,
    },
    'tuple': {
        '__len__': patchtuple.patch_tuple_len,
        '__getitem__': patchtuple.patch_tuple_getitem,
        '__contains__': patchtuple.patch_tuple_contains,  # probably not necessary
    },
    'dict': {
        '__getitem__': patchdictionary.patch_dictionary_getitem,
        '__setitem__': patchdictionary.patch_dictionary_setitem,
        '__contains__': patchdictionary.patch_dictionary_contains,
        '__iter__': patchdictionary.patch_dictionary_iter,
    },
}


def patch_with_module(class_: str, method_name: str, replacement_method):
    special_patch_methods[class_][method_name](replacement_method)


def set_import_replacement_method(module, class_, method_name, patched_func):
    patch_imports.replacement_import_methods.setdefault(module.__name__, dict())[
        method_name
    ] = patched_func
    #     (method_name, replacement_method)


replaced_methods = dict()
from .method_switch import MethodSwitch
from ..utils.utils import get_c_method


method_switches = set()


def create_patch(module, class_: str, method_name, replacement_method):
    if not callable(replacement_method):
        raise Exception('Given function is not callable!')

    if module.__name__ == 'builtins':
        if class_ is None:
            patching_method = patch_py_builtin_method
            original_method = getattr(builtins, method_name)
            class_to_patch = class_
        else:
            class_to_patch = non_builtin_types.get(class_, None)

            if class_to_patch is None:
                class_to_patch = getattr(module, class_)
            if class_to_patch is None:
                raise Exception('Given class is not defined in builtins!')

            py_defined_methods = pyo.py_method_def_by_class.get(class_to_patch, None)
            if py_defined_methods is not None and method_name in py_defined_methods:
                patching_method = patch_py_builtin_class_method
                original_method = get_py_builtin_class_method(
                    class_to_patch, method_name
                )

            else:
                print(class_, method_name)
                patching_method = patch_py_object_method
                original_method = get_c_method(class_to_patch, method_name)

    elif utils.is_user_defined_module(module):
        if class_ == None:
            original_method = getattr(module, method_name)
        else:
            class_to_patch = getattr(module, class_)
            original_method = getattr(class_to_patch, method_name)
        patching_method = patch_user_defined_method
        class_to_patch = class_

    else:
        original_method = None
        patching_method = set_import_replacement_method
        class_to_patch = None  # TODO add class

    global method_switches
    method_switches.add(
        MethodSwitch(
            patching_method,
            module,
            class_to_patch,
            method_name,
            original_method,
            replacement_method,
        )
    )


def apply():
    for m in method_switches:
        # print(m.module, m.class_, m.method_name, m.get_replacement_method())
        m.overwrite(m.module, m.class_, m.method_name, m.get_replacement_method())


def revert():
    for m in method_switches:
        m.overwrite(m.module, m.class_, m.method_name, m.get_original_method())
