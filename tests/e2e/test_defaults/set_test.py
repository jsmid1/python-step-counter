import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestSetMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_set_and(self):
        with RecodingActivated():
            x = {1, 2}
            x = x & {2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__and__'))

    def test_set_contains(self):
        with RecodingActivated():
            x = {1, 2, 3}
            result = 1 in x
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__contains__'))

    def test_set_eq(self):
        with RecodingActivated():
            x = {1, 2, 3}
            result = x == {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__eq__'))

    def test_set_ge(self):
        with RecodingActivated():
            x = {1, 2, 3}
            result = x >= {1, 2}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__ge__'))

    def test_set_gt(self):
        with RecodingActivated():
            x = {1, 2, 3}
            result = x > {1, 2}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__gt__'))

    def test_set_iand(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x &= {2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__iand__'))

    def test_set_ior(self):
        with RecodingActivated():
            x = {1, 2}
            x |= {3, 4}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__ior__'))

    def test_set_isub(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x -= {3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__isub__'))

    def test_set_iter(self):
        with RecodingActivated():
            x = {1, 2, 3}
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__iter__'))

    def test_set_ixor(self):
        with RecodingActivated():
            x = {1, 2}
            x ^= {2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__ixor__'))

    def test_set_le(self):
        with RecodingActivated():
            x = {1, 2}
            result = x <= {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__le__'))

    def test_set_len(self):
        with RecodingActivated():
            x = {1, 2, 3}
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__len__'))

    def test_set_lt(self):
        with RecodingActivated():
            x = {1, 2}
            result = x < {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__lt__'))

    def test_set_ne(self):
        with RecodingActivated():
            x = {1, 2, 3}
            result = x != {1, 2}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__ne__'))

    def test_set_or(self):
        with RecodingActivated():
            x = {1, 2}
            x = x | {3, 4}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__or__'))

    def test_set_sub(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x = x - {2}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__sub__'))

    def test_set_xor(self):
        with RecodingActivated():
            x = {1, 2}
            x = x ^ {2, 3}
        self.assertTrue(is_recorded(self.recorder, builtins, set, '__xor__'))

    # Non-dunder methods
    def test_set_add(self):
        with RecodingActivated():
            x = {1, 2}
            x.add(3)
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'add'))

    def test_set_clear(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x.clear()
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'clear'))

    def test_set_copy(self):
        with RecodingActivated():
            x = {1, 2, 3}
            y = x.copy()
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'copy'))

    def test_set_difference(self):
        with RecodingActivated():
            x = {1, 2, 3}
            y = x.difference({2})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'difference'))

    def test_set_discard(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x.discard(2)
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'discard'))

    def test_set_intersection(self):
        with RecodingActivated():
            x = {1, 2, 3}
            y = x.intersection({2, 3, 4})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'intersection'))

    def test_set_isdisjoint(self):
        with RecodingActivated():
            x = {1, 2}
            y = x.isdisjoint({3, 4})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'isdisjoint'))

    def test_set_issubset(self):
        with RecodingActivated():
            x = {1, 2}
            y = x.issubset({1, 2, 3})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'issubset'))

    def test_set_issuperset(self):
        with RecodingActivated():
            x = {1, 2, 3}
            y = x.issuperset({1, 2})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'issuperset'))

    def test_set_pop(self):
        with RecodingActivated():
            x = {1, 2, 3}
            el = x.pop()
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'pop'))

    def test_set_remove(self):
        with RecodingActivated():
            x = {1, 2, 3}
            x.remove(2)
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'remove'))

    def test_set_union(self):
        with RecodingActivated():
            x = {1, 2}
            y = x.union({3, 4})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'union'))

    def test_set_update(self):
        with RecodingActivated():
            x = {1, 2}
            x.update({3, 4})
        self.assertTrue(is_recorded(self.recorder, builtins, set, 'update'))
