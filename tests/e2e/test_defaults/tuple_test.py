import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded


class TestTupleMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_tuple_add(self):
        with recording_activated():
            x = (1, 2)
            x + (3, 4)
        self.assertTrue(is_recorded(self.recorder, tuple, '__add__'))

    def test_tuple_contains(self):
        with recording_activated():
            x = (1, 2, 3)
            2 in x
        self.assertTrue(is_recorded(self.recorder, tuple, '__contains__'))

    def test_tuple_getitem(self):
        with recording_activated():
            x = (1, 2, 3)
            _ = x[1]
        self.assertTrue(is_recorded(self.recorder, tuple, '__getitem__'))

    def test_tuple_count(self):
        with recording_activated():
            x = (1, 2, 1, 3)
            x.count(1)
        self.assertTrue(is_recorded(self.recorder, tuple, 'count'))

    def test_tuple_index(self):
        with recording_activated():
            x = (1, 2, 3)
            x.index(2)
        self.assertTrue(is_recorded(self.recorder, tuple, 'index'))

    def test_tuple_eq(self):
        with recording_activated():
            x = (1, 2)
            x == (1, 2)
        self.assertTrue(is_recorded(self.recorder, tuple, '__eq__'))

    def test_tuple_ne(self):
        with recording_activated():
            x = (1, 2)
            x != (2, 1)
        self.assertTrue(is_recorded(self.recorder, tuple, '__ne__'))

    def test_tuple_len(self):
        with recording_activated():
            x = (1, 2, 3)
            len(x)
        self.assertTrue(is_recorded(self.recorder, tuple, '__len__'))

    def test_tuple_mul(self):
        with recording_activated():
            x = (1, 2)
            x * 2
        self.assertTrue(is_recorded(self.recorder, tuple, '__mul__'))

    def test_tuple_iter(self):
        with recording_activated():
            x = (1, 2, 3)
            iter(x)
        self.assertTrue(is_recorded(self.recorder, tuple, '__iter__'))

    def test_tuple_str(self):
        with recording_activated():
            x = (1, 2, 3)
            str(x)
        self.assertTrue(is_recorded(self.recorder, tuple, '__str__'))
