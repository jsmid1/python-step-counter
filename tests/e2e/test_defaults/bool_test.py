import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import builtins
import operator


class TestBoolMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bool_abs(self):
        x = True
        with RecodingActivated():
            abs(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__abs__'))

    def test_bool_add(self):
        x = True
        with RecodingActivated():
            x = True + x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__add__'))

    def test_bool_and(self):
        x = True
        with RecodingActivated():
            x = True & x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__and__'))

    @unittest.skip('Not used')
    def test_bool_bool(self):
        x = True
        with RecodingActivated():
            x = bool(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__bool__'))

    def test_bool_eq(self):
        x = True
        with RecodingActivated():
            x = True == x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__eq__'))

    def test_bool_float(self):
        x = True
        with RecodingActivated():
            x = float(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__float__'))

    @unittest.skip(
        ' Would be recorded under operator module but import of operator is not allowed'
    )
    def test_bool_index(self):
        x = True
        with RecodingActivated():
            x = operator.index(x)

        self.assertTrue(is_recorded(self.recorder, operator, None, '__index__'))

    def test_bool_int(self):
        x = True
        with RecodingActivated():
            x = int(x)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__int__'))

    def test_bool_invert(self):
        x = True
        with RecodingActivated():
            x = ~x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__invert__'))

    def test_bool_lshift(self):
        x = True
        with RecodingActivated():
            x = x << 2
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__lshift__'))

    def test_bool_mod(self):
        x = True
        with RecodingActivated():
            x = x % True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__mod__'))

    def test_bool_mul(self):
        x = True
        with RecodingActivated():
            x = x * True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__mul__'))

    def test_bool_ne(self):
        x = True
        with RecodingActivated():
            x = x != False
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__ne__'))

    def test_bool_neg(self):
        x = True
        with RecodingActivated():
            x = -x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__neg__'))

    def test_bool_or(self):
        x = True
        with RecodingActivated():
            x = x | True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__or__'))

    def test_bool_pos(self):
        x = True
        with RecodingActivated():
            x = +x
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__pos__'))

    def test_bool_pow(self):
        x = True
        with RecodingActivated():
            x = pow(x, True)
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__pow__'))

    def test_bool_rshift(self):
        x = True
        with RecodingActivated():
            x = x >> 2
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__rshift__'))

    def test_bool_sub(self):
        x = True
        with RecodingActivated():
            x = x - True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__sub__'))

    def test_bool_truediv(self):
        x = True
        with RecodingActivated():
            x = x / True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__truediv__'))

    def test_bool_xor(self):
        x = True
        with RecodingActivated():
            x = x ^ True
        self.assertTrue(is_recorded(self.recorder, builtins, bool, '__xor__'))

    def test_bool_as_integer_ratio(self):
        x = True
        with RecodingActivated():
            x.as_integer_ratio()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'as_integer_ratio'))

    def test_bool_bit_length(self):
        x = True
        with RecodingActivated():
            x.bit_length()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'bit_length'))

    def test_bool_conjugate(self):
        x = True
        with RecodingActivated():
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, builtins, bool, 'conjugate'))
