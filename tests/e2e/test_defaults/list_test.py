import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


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
        with RecodingActivated():
            x = [1]
            x + [2]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__add__'))

    def test_list_contains(self):
        with RecodingActivated():
            x = [1, 2, 3]
            1 in x
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__contains__'))

    @unittest.skip('Setitem internally, banned in restrict')
    def test_list_delitem(self):
        with RecodingActivated():
            x = [1, 2, 3]
            del x[1]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__delitem__'))

    def test_list_eq(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x == [1, 2, 3]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__eq__'))

    def test_list_getitem(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x[1]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__getitem__'))

    def test_list_iadd(self):
        with RecodingActivated():
            x = [1, 2]
            x += [3, 4]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__iadd__'))

    def test_list_imul(self):
        with RecodingActivated():
            x = [1, 2]
            x *= 2
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__imul__'))

    def test_list_iter(self):
        with RecodingActivated():
            x = [1, 2, 3]
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__iter__'))

    def test_list_len(self):
        with RecodingActivated():
            x = [1, 2, 3]
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__len__'))

    def test_list_mul(self):
        with RecodingActivated():
            x = [1, 2]
            x * 2
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__mul__'))

    def test_list_ne(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x != [1, 2]
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__ne__'))

    @unittest.skip('Not recorder')
    def test_list_setitem(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x[1] = 4
        self.assertTrue(is_recorded(self.recorder, builtins, list, '__setitem__'))

    def test_list_append(self):
        with RecodingActivated():
            x = [1, 2]
            x.append(3)
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'append'))

    def test_list_clear(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x.clear()
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'clear'))

    def test_list_copy(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x.copy()
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'copy'))

    def test_list_count(self):
        with RecodingActivated():
            x = [1, 1, 2, 3]
            x.count(1)
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'count'))

    def test_list_extend(self):
        with RecodingActivated():
            x = [1, 2]
            x.extend([3, 4])
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'extend'))

    def test_list_index(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x.index(2)
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'index'))

    def test_list_insert(self):
        with RecodingActivated():
            x = [1, 3]
            x.insert(1, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'insert'))

    def test_list_pop(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x.pop()
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'pop'))

    def test_list_remove(self):
        with RecodingActivated():
            x = [1, 2, 3]
            x.remove(2)
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'remove'))

    def test_list_reverse(self):
        with RecodingActivated():
            x = [3, 2, 1]
            x.reverse()
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'reverse'))

    def test_list_sort(self):
        with RecodingActivated():
            x = [2, 3, 1]
            x.sort()
        self.assertTrue(is_recorded(self.recorder, builtins, list, 'sort'))
