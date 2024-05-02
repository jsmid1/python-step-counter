import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

from collections import deque
import collections

py_minor_version = sys.version_info[1]


class TestIntMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_deque_add(self):
        with RecodingActivated():
            x = deque([1, 2])
            x + deque([3, 4])
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__add__'))

    def test_deque_bool(self):
        with RecodingActivated():
            bool(deque([1, 2]))
        self.assertTrue(
            is_recorded(
                self.recorder,
                collections,
                deque,
                '__bool__' if py_minor_version == 10 else '__len__',
            )
        )

    def test_deque_contains(self):
        with RecodingActivated():
            2 in deque([1, 2, 3])
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__contains__'))

    def test_deque_copy(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.copy()
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'copy'))

    @unittest.skip('Setitem internally, banned in restrict')
    def test_deque_delitem(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            del x[1]
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__delitem__'))

    def test_deque_eq(self):
        with RecodingActivated():
            deque([1, 2]) == deque([1, 2])
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__eq__'))

    def test_deque_getitem(self):
        with RecodingActivated():
            _ = deque([1, 2, 3])[1]
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__getitem__'))

    def test_deque_len(self):
        with RecodingActivated():
            len(deque([1, 2, 3]))
        self.assertTrue(is_recorded(self.recorder, collections, deque, '__len__'))

    def test_deque_append(self):
        with RecodingActivated():
            x = deque([1, 2])
            x.append(3)
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'append'))

    def test_deque_clear(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.clear()
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'clear'))

    def test_deque_extend(self):
        with RecodingActivated():
            x = deque([1, 2])
            x.extend([3, 4])
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'extend'))

    def test_deque_pop(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.pop()
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'pop'))

    def test_deque_popleft(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.popleft()
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'popleft'))

    def test_deque_reverse(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.reverse()
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'reverse'))

    def test_deque_rotate(self):
        with RecodingActivated():
            x = deque([1, 2, 3])
            x.rotate(1)
        self.assertTrue(is_recorded(self.recorder, collections, deque, 'rotate'))
