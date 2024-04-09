import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import builtins


class TestRangeMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_range_bool(self):
        with recording_activated():
            x = bool(range(1))
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__bool__'))

    def test_range_contains(self):
        with recording_activated():
            2 in range(1, 3)
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__contains__'))

    def test_range_eq(self):
        with recording_activated():
            range(1, 3) == range(1, 3)
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__eq__'))

    def test_range_getitem(self):
        with recording_activated():
            _ = range(10)[1]
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__getitem__'))

    def test_range_iter(self):
        with recording_activated():
            iter(range(10))
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__iter__'))

    def test_range_len(self):
        with recording_activated():
            len(range(10))
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__len__'))

    def test_range_ne(self):
        with recording_activated():
            range(1, 3) != range(4, 6)
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__ne__'))

    def test_range_reversed(self):
        with recording_activated():
            list(reversed(range(10)))
        self.assertTrue(is_recorded(self.recorder, builtins, range, '__reversed__'))

    def test_range_count(self):
        with recording_activated():
            range(10).count(2)
        self.assertTrue(is_recorded(self.recorder, builtins, range, 'count'))

    def test_range_index(self):
        with recording_activated():
            range(1, 10).index(2)
        self.assertTrue(is_recorded(self.recorder, builtins, range, 'index'))
