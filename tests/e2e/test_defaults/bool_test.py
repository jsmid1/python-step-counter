import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import builtins
import operator


class TestBoolMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bool_abs(self):
        with recording_activated():
            x = abs(True)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__abs__'))

    def test_bool_add(self):
        with recording_activated():
            x = True
            x = True + x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__add__'))

    def test_bool_and(self):
        with recording_activated():
            x = True
            x = True & x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__and__'))

    @unittest.skip('Not used')
    def test_bool_bool(self):
        with recording_activated():
            x = True
            x = bool(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__bool__'))

    def test_bool_eq(self):
        with recording_activated():
            x = True
            x = True == x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__eq__'))

    def test_bool_float(self):
        with recording_activated():
            x = True
            x = float(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__float__'))

    @unittest.skip(
        ' Would be recorded under operator module but import of operator is nor allowed'
    )
    def test_bool_index(self):
        with recording_activated():
            x = True
            x = operator.index(x)

        self.assertTrue(is_recorded(self.recorder, operator, None, '__index__'))

    def test_bool_int(self):
        with recording_activated():
            x = True
            x = int(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__int__'))

    def test_bool_invert(self):
        with recording_activated():
            x = True
            x = ~x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__invert__'))

    def test_bool_lshift(self):
        with recording_activated():
            x = True
            x = x << 2
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__lshift__'))

    def test_bool_mod(self):
        with recording_activated():
            x = True
            x = x % True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__mod__'))

    def test_bool_mul(self):
        with recording_activated():
            x = True
            x = x * True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__mul__'))

    def test_bool_ne(self):
        with recording_activated():
            x = True
            x = x != False
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__ne__'))

    def test_bool_neg(self):
        with recording_activated():
            x = True
            x = -x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__neg__'))

    def test_bool_or(self):
        with recording_activated():
            x = True
            x = x | True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__or__'))

    def test_bool_pos(self):
        with recording_activated():
            x = True
            x = +x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__pos__'))

    def test_bool_pow(self):
        with recording_activated():
            x = True
            x = pow(x, True)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__pow__'))

    def test_bool_rshift(self):
        with recording_activated():
            x = True
            x = x >> 2
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__rshift__'))

    def test_bool_sub(self):
        with recording_activated():
            x = True
            x = x - True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__sub__'))

    def test_bool_truediv(self):
        with recording_activated():
            x = True
            x = x / True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__truediv__'))

    def test_bool_xor(self):
        with recording_activated():
            x = True
            x = x ^ True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__xor__'))

    # Testing non-dunder methods that make sense for bool
    def test_bool_as_integer_ratio(self):
        with recording_activated():
            x = True
            x.as_integer_ratio()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'as_integer_ratio'))

    def test_bool_bit_length(self):
        with recording_activated():
            x = True
            x.bit_length()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'bit_length'))

    def test_bool_conjugate(self):
        with recording_activated():
            x = True
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'conjugate'))
