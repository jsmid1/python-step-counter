import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded


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
        with recording_activated():
            x = {1, 2}
            x = x & {2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__and__'))

    def test_set_contains(self):
        with recording_activated():
            x = {1, 2, 3}
            result = 1 in x
        self.assertTrue(is_recorded(self.recorder, set, '__contains__'))

    def test_set_eq(self):
        with recording_activated():
            x = {1, 2, 3}
            result = x == {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__eq__'))

    def test_set_ge(self):
        with recording_activated():
            x = {1, 2, 3}
            result = x >= {1, 2}
        self.assertTrue(is_recorded(self.recorder, set, '__ge__'))

    def test_set_gt(self):
        with recording_activated():
            x = {1, 2, 3}
            result = x > {1, 2}
        self.assertTrue(is_recorded(self.recorder, set, '__gt__'))

    def test_set_iand(self):
        with recording_activated():
            x = {1, 2, 3}
            x &= {2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__iand__'))

    def test_set_ior(self):
        with recording_activated():
            x = {1, 2}
            x |= {3, 4}
        self.assertTrue(is_recorded(self.recorder, set, '__ior__'))

    def test_set_isub(self):
        with recording_activated():
            x = {1, 2, 3}
            x -= {3}
        self.assertTrue(is_recorded(self.recorder, set, '__isub__'))

    def test_set_iter(self):
        with recording_activated():
            x = {1, 2, 3}
            iter(x)
        self.assertTrue(is_recorded(self.recorder, set, '__iter__'))

    def test_set_ixor(self):
        with recording_activated():
            x = {1, 2}
            x ^= {2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__ixor__'))

    def test_set_le(self):
        with recording_activated():
            x = {1, 2}
            result = x <= {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__le__'))

    def test_set_len(self):
        with recording_activated():
            x = {1, 2, 3}
            len(x)
        self.assertTrue(is_recorded(self.recorder, set, '__len__'))

    def test_set_lt(self):
        with recording_activated():
            x = {1, 2}
            result = x < {1, 2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__lt__'))

    def test_set_ne(self):
        with recording_activated():
            x = {1, 2, 3}
            result = x != {1, 2}
        self.assertTrue(is_recorded(self.recorder, set, '__ne__'))

    def test_set_or(self):
        with recording_activated():
            x = {1, 2}
            x = x | {3, 4}
        self.assertTrue(is_recorded(self.recorder, set, '__or__'))

    def test_set_sub(self):
        with recording_activated():
            x = {1, 2, 3}
            x = x - {2}
        self.assertTrue(is_recorded(self.recorder, set, '__sub__'))

    def test_set_xor(self):
        with recording_activated():
            x = {1, 2}
            x = x ^ {2, 3}
        self.assertTrue(is_recorded(self.recorder, set, '__xor__'))

    # Non-dunder methods
    def test_set_add(self):
        with recording_activated():
            x = {1, 2}
            x.add(3)
        self.assertTrue(is_recorded(self.recorder, set, 'add'))

    def test_set_clear(self):
        with recording_activated():
            x = {1, 2, 3}
            x.clear()
        self.assertTrue(is_recorded(self.recorder, set, 'clear'))

    def test_set_copy(self):
        with recording_activated():
            x = {1, 2, 3}
            y = x.copy()
        self.assertTrue(is_recorded(self.recorder, set, 'copy'))

    def test_set_difference(self):
        with recording_activated():
            x = {1, 2, 3}
            y = x.difference({2})
        self.assertTrue(is_recorded(self.recorder, set, 'difference'))

    def test_set_discard(self):
        with recording_activated():
            x = {1, 2, 3}
            x.discard(2)
        self.assertTrue(is_recorded(self.recorder, set, 'discard'))

    def test_set_intersection(self):
        with recording_activated():
            x = {1, 2, 3}
            y = x.intersection({2, 3, 4})
        self.assertTrue(is_recorded(self.recorder, set, 'intersection'))

    def test_set_isdisjoint(self):
        with recording_activated():
            x = {1, 2}
            y = x.isdisjoint({3, 4})
        self.assertTrue(is_recorded(self.recorder, set, 'isdisjoint'))

    def test_set_issubset(self):
        with recording_activated():
            x = {1, 2}
            y = x.issubset({1, 2, 3})
        self.assertTrue(is_recorded(self.recorder, set, 'issubset'))

    def test_set_issuperset(self):
        with recording_activated():
            x = {1, 2, 3}
            y = x.issuperset({1, 2})
        self.assertTrue(is_recorded(self.recorder, set, 'issuperset'))

    def test_set_pop(self):
        with recording_activated():
            x = {1, 2, 3}
            el = x.pop()
        self.assertTrue(is_recorded(self.recorder, set, 'pop'))

    def test_set_remove(self):
        with recording_activated():
            x = {1, 2, 3}
            x.remove(2)
        self.assertTrue(is_recorded(self.recorder, set, 'remove'))

    def test_set_union(self):
        with recording_activated():
            x = {1, 2}
            y = x.union({3, 4})
        self.assertTrue(is_recorded(self.recorder, set, 'union'))

    def test_set_update(self):
        with recording_activated():
            x = {1, 2}
            x.update({3, 4})
        self.assertTrue(is_recorded(self.recorder, set, 'update'))
