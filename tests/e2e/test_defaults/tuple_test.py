import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestTupleMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_tuple_add(self):
        with RecodingActivated():
            x = (1, 2)
            x + (3, 4)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__add__'))

    def test_tuple_contains(self):
        with RecodingActivated():
            x = (1, 2, 3)
            2 in x
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__contains__'))

    def test_tuple_getitem(self):
        with RecodingActivated():
            x = (1, 2, 3)
            _ = x[1]
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__getitem__'))

    def test_tuple_count(self):
        with RecodingActivated():
            x = (1, 2, 1, 3)
            x.count(1)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, 'count'))

    def test_tuple_index(self):
        with RecodingActivated():
            x = (1, 2, 3)
            x.index(2)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, 'index'))

    def test_tuple_eq(self):
        with RecodingActivated():
            x = (1, 2)
            x == (1, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__eq__'))

    def test_tuple_ne(self):
        with RecodingActivated():
            x = (1, 2)
            x != (2, 1)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__ne__'))

    def test_tuple_len(self):
        with RecodingActivated():
            x = (1, 2, 3)
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__len__'))

    def test_tuple_mul(self):
        with RecodingActivated():
            x = (1, 2)
            x * 2
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__mul__'))

    def test_tuple_iter(self):
        with RecodingActivated():
            x = (1, 2, 3)
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__iter__'))

    def test_tuple_str(self):
        with RecodingActivated():
            x = (1, 2, 3)
            str(x)
        self.assertTrue(is_recorded(self.recorder, builtins, tuple, '__str__'))
