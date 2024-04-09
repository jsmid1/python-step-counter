import unittest
import builtins
import ctypes

from src.step_counting.patch.patching import (
    patch_imports,
    patch_py_builtin_method,
    patch_py_object_method,
    patch_py_std_class_method,
    patch_py_object_method_with_type,
)

from src.step_counting.utils.methods import get_c_method


def generic_replacement_method_str(*args, **kwargs):
    return 'patched'


def generic_replacement_method_int(*args, **kwargs):
    return 42


class TestPatchingMethods(unittest.TestCase):
    def test_patch_py_object_method_with_type(self):
        class_ = int
        tp_name = 'tp_as_number'
        method_name_c = 'nb_add'
        method_name_py = '__add__'

        patch_py_object_method_with_type(
            class_,
            tp_name,
            method_name_c,
            ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object),
            generic_replacement_method_int,
        )

        method = get_c_method(class_, method_name_py)

        self.assertEqual(method(1, 1), 42)

    def test_patch_py_builtin_method(self):
        method_name = 'print'

        patch_py_builtin_method(
            builtins, None, method_name, generic_replacement_method_int
        )

        method = getattr(builtins, method_name)

        self.assertEqual(method, generic_replacement_method_int)

    def test_patch_py_builtin_class_method(self):
        class_ = int
        method_name = 'as_integer_ratio'

        patch_py_std_class_method(
            builtins, class_, method_name, generic_replacement_method_int
        )

        method = getattr(class_, method_name)

        self.assertEqual(method, generic_replacement_method_int)

    def test_patch_py_object_tp_method(self):
        class_ = list
        method_name = '__add__'

        patch_py_object_method(
            None, class_, method_name, generic_replacement_method_str
        )

        method = get_c_method(class_, method_name)

        self.assertEqual(method(1, 1), 'patched')

    def test_patch_py_object_method(self):
        class_ = int
        method_name = '__str__'

        patch_py_object_method(
            None, class_, method_name, generic_replacement_method_str
        )

        method = get_c_method(class_, method_name)

        self.assertEqual(method(1), 'patched')


if __name__ == '__main__':
    unittest.main()
