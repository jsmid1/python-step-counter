import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestEnumerateMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(None, self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_enumerate_eq(self):
        with RecodingActivated():
            enumerate([1]) == enumerate([1])
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__eq__'))

    def test_enumerate_iter(self):
        with RecodingActivated():
            iter(enumerate([1]))
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__iter__'))

    def test_enumerate_hash(self):
        with RecodingActivated():
            hash(enumerate([1]))
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__hash__'))

    def test_enumerate_reduce(self):
        with RecodingActivated():
            enumerate([1]).__reduce__()
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__reduce__'))

    def test_enumerate_reduce_ex(self):
        with RecodingActivated():
            enumerate([1]).__reduce_ex__(1)
        self.assertTrue(
            is_recorded(self.recorder, builtins, enumerate, '__reduce_ex__')
        )

    def test_enumerate_repr(self):
        with RecodingActivated():
            repr(enumerate([1]))
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__repr__'))

    def test_enumerate_str(self):
        with RecodingActivated():
            str(enumerate([1]))
        self.assertTrue(is_recorded(self.recorder, builtins, enumerate, '__str__'))
