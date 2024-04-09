import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestComplexMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_slice_eq(self):
        with RecodingActivated():
            x = slice(1, 5, 2)
            y = slice(1, 5, 2)
            x == y
        self.assertTrue(is_recorded(self.recorder, builtins, slice, '__eq__'))

    def test_slice_indices(self):
        with RecodingActivated():
            x = slice(1, 5, 2)
            result = x.indices(10)
        self.assertTrue(is_recorded(self.recorder, builtins, slice, 'indices'))

    def test_slice_str(self):
        with RecodingActivated():
            x = str(slice(1, 5, 2))
        self.assertTrue(is_recorded(self.recorder, builtins, slice, '__str__'))

    def test_slice_repr(self):
        with RecodingActivated():
            x = repr(slice(1, 5, 2))
        self.assertTrue(is_recorded(self.recorder, builtins, slice, '__repr__'))

    @unittest.skip('Can not be called directly withou slice.__reduce__')
    def test_slice_reduce(self):
        with RecodingActivated():
            x = slice(1, 5, 2).__reduce__()
        self.assertTrue(is_recorded(self.recorder, builtins, slice, '__reduce__'))
