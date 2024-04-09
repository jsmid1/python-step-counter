import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins

dict_keys = type({}.keys())
dict_items = type({}.items())


class TestDictkeysMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    # Can be recorded under dict_items
    def test_dict_keys_and(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys()
            y = {'b': 2, 'c': 3}.keys()
            x & y
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__and__')
            or is_recorded(self.recorder, builtins, dict_items, '__contains__')
        )

    # Can be recorded under dict_items
    def test_dict_keys_or(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys()
            y = {'c': 3}.keys()
            x | y
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__or__')
            or is_recorded(self.recorder, builtins, dict_items, '__contains__')
        )

    # Can be recorded under dict_items
    def test_dict_keys_xor(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys()
            y = {'b': 2, 'c': 3}.keys()
            x ^ y
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__xor__')
            or is_recorded(self.recorder, builtins, dict_items, '__contains__')
        )

    # Can be recorded under dict_items
    def test_dict_keys_sub(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys()
            y = {'b': 2}.keys()
            x - y
        self.assertTrue(
            is_recorded(self.recorder, builtins, dict_keys, '__sub__')
            or is_recorded(self.recorder, builtins, dict_items, '__contains__')
        )

    def test_dict_keys_contains(self):
        with RecodingActivated():
            'a' in {'a': 1, 'b': 2}.keys()
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, '__contains__'))

    def test_dict_keys_eq(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys() == {'a': 1, 'b': 2}.keys()
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, '__eq__'))

    def test_dict_keys_ne(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys() != {'a': 2}.keys()
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, '__ne__'))

    def test_dict_keys_iter(self):
        with RecodingActivated():
            iter({'a': 1, 'b': 2}.keys())
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, '__iter__'))

    def test_dict_keys_len(self):
        with RecodingActivated():
            len({'a': 1, 'b': 2}.keys())
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, '__len__'))

    def test_dict_keys_isdisjoint(self):
        with RecodingActivated():
            x = {'a': 1, 'b': 2}.keys()
            y = {'c': 3, 'd': 4}.keys()
            x.isdisjoint(y)
        self.assertTrue(is_recorded(self.recorder, builtins, dict_keys, 'isdisjoint'))
