import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins

py_minor_version = sys.version_info[1]


class TestFrozensetMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_frozenset_and(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            y = x & frozenset([2, 3])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__and__'))

    # Uses set method
    def test_frozenset_contains(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = 1 in x
        self.assertTrue(
            is_recorded(
                self.recorder,
                builtins,
                set if py_minor_version == 10 else frozenset,
                '__contains__',
            )
        )

    def test_frozenset_eq(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = x == frozenset([1, 2, 3])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__eq__'))

    def test_frozenset_ge(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = x >= frozenset([1, 2])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__ge__'))

    def test_frozenset_gt(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = x > frozenset([1, 2])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__gt__'))

    def test_frozenset_iter(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            iter(x)
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__iter__'))

    def test_frozenset_le(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            result = x <= frozenset([1, 2, 3])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__le__'))

    # Uses set method
    def test_frozenset_len(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            len(x)

        self.assertTrue(
            is_recorded(
                self.recorder,
                builtins,
                set if py_minor_version == 10 else frozenset,
                '__len__',
            )
        )

    def test_frozenset_lt(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            result = x < frozenset([1, 2, 3])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__lt__'))

    def test_frozenset_ne(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = x != frozenset([1, 2])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__ne__'))

    def test_frozenset_or(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            y = x | frozenset([3, 4])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__or__'))

    def test_frozenset_sub(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            y = x - frozenset([2])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__sub__'))

    def test_frozenset_xor(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            y = x ^ frozenset([2, 3])
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, '__xor__'))

    # Non-dunder methods
    def test_frozenset_copy(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            y = x.copy()
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'copy'))

    def test_frozenset_difference(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            y = x.difference(frozenset([2]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'difference'))

    def test_frozenset_intersection(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            y = x.intersection(frozenset([2, 3, 4]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'intersection'))

    def test_frozenset_isdisjoint(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            result = x.isdisjoint(frozenset([3, 4]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'isdisjoint'))

    def test_frozenset_issubset(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            result = x.issubset(frozenset([1, 2, 3]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'issubset'))

    def test_frozenset_issuperset(self):
        with RecodingActivated():
            x = frozenset([1, 2, 3])
            result = x.issuperset(frozenset([1, 2]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'issuperset'))

    def test_frozenset_symmetric_difference(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            y = x.symmetric_difference(frozenset([2, 3]))
        self.assertTrue(
            is_recorded(self.recorder, builtins, frozenset, 'symmetric_difference')
        )

    def test_frozenset_union(self):
        with RecodingActivated():
            x = frozenset([1, 2])
            y = x.union(frozenset([3, 4]))
        self.assertTrue(is_recorded(self.recorder, builtins, frozenset, 'union'))
