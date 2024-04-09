import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins

dict_items = type({}.items())
dict_keys = type({}.keys())


class TestDictItemsMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})
        self.items1 = {'a': 1, 'b': 2}.items()
        self.items2 = {'b': 2, 'c': 3}.items()

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    # Can be recorded under dict_keys or dict_items
    def test_dict_items_and(self):
        with RecodingActivated():
            self.items1 & self.items2
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__and__')
            or is_recorded(self.recorder, builtins, dict_items, '__and__')
        )

    # Can be recorded under dict_keys or dict_items
    def test_dict_items_or(self):
        with RecodingActivated():
            self.items1 | self.items2
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__or__')
            or is_recorded(self.recorder, builtins, dict_items, '__or__')
        )

    # Can be recorded under dict_keys or dict_items
    def test_dict_items_xor(self):
        with RecodingActivated():
            self.items1 ^ self.items2
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__xor__')
            or is_recorded(self.recorder, builtins, dict_items, '__xor__')
        )

    # Can be recorded under dict_keys or dict_items
    def test_dict_items_sub(self):
        with RecodingActivated():
            self.items1 - self.items2
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__sub__')
            or is_recorded(self.recorder, builtins, dict_items, '__sub__')
        )

    def test_dict_items_contains(self):
        with RecodingActivated():
            ('a', 1) in self.items1
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_items, '__contains__')
        )

    def test_dict_items_eq(self):
        with RecodingActivated():
            self.items1 == self.items2
        self.assertTrue(is_recorded(self.recorder, builtins, dict_items, '__eq__'))

    def test_dict_items_ne(self):
        with RecodingActivated():
            self.items1 != self.items2
        self.assertTrue(is_recorded(self.recorder, builtins, dict_items, '__ne__'))

    def test_dict_items_iter(self):
        with RecodingActivated():
            iter(self.items1)
        self.assertTrue(is_recorded(self.recorder, builtins, dict_items, '__iter__'))

    def test_dict_items_len(self):
        with RecodingActivated():
            len(self.items1)
        self.assertTrue(is_recorded(self.recorder, builtins, dict_items, '__len__'))

    def test_dict_items_isdisjoint(self):
        with RecodingActivated():
            self.items1.isdisjoint(self.items2)
        self.assertTrue(is_recorded(self.recorder, builtins, dict_items, 'isdisjoint'))
