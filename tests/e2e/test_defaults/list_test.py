import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import math


class TestDictMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_list_add(self):
        with recording_activated():
            x = [1]
            x + [2]
        self.assertTrue(is_recorded(self.recorder, list, '__add__'))

    def test_list_contains(self):
        with recording_activated():
            x = [1, 2, 3]
            1 in x
        self.assertTrue(is_recorded(self.recorder, list, '__contains__'))

    @unittest.skip('Setitem internally, banned in restrict')
    def test_list_delitem(self):
        with recording_activated():
            x = [1, 2, 3]
            del x[1]
        self.assertTrue(is_recorded(self.recorder, list, '__delitem__'))

    def test_list_eq(self):
        with recording_activated():
            x = [1, 2, 3]
            x == [1, 2, 3]
        self.assertTrue(is_recorded(self.recorder, list, '__eq__'))

    def test_list_getitem(self):
        with recording_activated():
            x = [1, 2, 3]
            x[1]
        self.assertTrue(is_recorded(self.recorder, list, '__getitem__'))

    def test_list_iadd(self):
        with recording_activated():
            x = [1, 2]
            x += [3, 4]
        self.assertTrue(is_recorded(self.recorder, list, '__iadd__'))

    def test_list_imul(self):
        with recording_activated():
            x = [1, 2]
            x *= 2
        self.assertTrue(is_recorded(self.recorder, list, '__imul__'))

    def test_list_iter(self):
        with recording_activated():
            x = [1, 2, 3]
            iter(x)
        self.assertTrue(is_recorded(self.recorder, list, '__iter__'))

    def test_list_len(self):
        with recording_activated():
            x = [1, 2, 3]
            len(x)
        self.assertTrue(is_recorded(self.recorder, list, '__len__'))

    def test_list_mul(self):
        with recording_activated():
            x = [1, 2]
            x * 2
        self.assertTrue(is_recorded(self.recorder, list, '__mul__'))

    def test_list_ne(self):
        with recording_activated():
            x = [1, 2, 3]
            x != [1, 2]
        self.assertTrue(is_recorded(self.recorder, list, '__ne__'))

    @unittest.skip('Not recorder')
    def test_list_setitem(self):
        with recording_activated():
            x = [1, 2, 3]
            x[1] = 4
        self.assertTrue(is_recorded(self.recorder, list, '__setitem__'))

    def test_list_append(self):
        with recording_activated():
            x = [1, 2]
            x.append(3)
        self.assertTrue(is_recorded(self.recorder, list, 'append'))

    def test_list_clear(self):
        with recording_activated():
            x = [1, 2, 3]
            x.clear()
        self.assertTrue(is_recorded(self.recorder, list, 'clear'))

    def test_list_copy(self):
        with recording_activated():
            x = [1, 2, 3]
            x.copy()
        self.assertTrue(is_recorded(self.recorder, list, 'copy'))

    def test_list_count(self):
        with recording_activated():
            x = [1, 1, 2, 3]
            x.count(1)
        self.assertTrue(is_recorded(self.recorder, list, 'count'))

    def test_list_extend(self):
        with recording_activated():
            x = [1, 2]
            x.extend([3, 4])
        self.assertTrue(is_recorded(self.recorder, list, 'extend'))

    def test_list_index(self):
        with recording_activated():
            x = [1, 2, 3]
            x.index(2)
        self.assertTrue(is_recorded(self.recorder, list, 'index'))

    def test_list_insert(self):
        with recording_activated():
            x = [1, 3]
            x.insert(1, 2)
        self.assertTrue(is_recorded(self.recorder, list, 'insert'))

    def test_list_pop(self):
        with recording_activated():
            x = [1, 2, 3]
            x.pop()
        self.assertTrue(is_recorded(self.recorder, list, 'pop'))

    def test_list_remove(self):
        with recording_activated():
            x = [1, 2, 3]
            x.remove(2)
        self.assertTrue(is_recorded(self.recorder, list, 'remove'))

    def test_list_reverse(self):
        with recording_activated():
            x = [3, 2, 1]
            x.reverse()
        self.assertTrue(is_recorded(self.recorder, list, 'reverse'))

    def test_list_sort(self):
        with recording_activated():
            x = [2, 3, 1]
            x.sort()
        self.assertTrue(is_recorded(self.recorder, list, 'sort'))
