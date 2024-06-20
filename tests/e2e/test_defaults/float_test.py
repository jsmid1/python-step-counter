import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import math
import builtins


class TestFloatMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(None, self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_float_abs(self):
        with RecodingActivated():
            x = -1.0
            abs(x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__abs__'))

    def test_float_add(self):
        with RecodingActivated():
            x = 1.0
            x + 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__add__'))

    def test_float_bool(self):
        with RecodingActivated():
            x = 1.0
            bool(x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__bool__'))

    @unittest.skip('Never used')
    def test_float_ceil(self):
        with RecodingActivated():
            x = 1.2
            math.ceil(x)
        self.assertTrue(is_recorded(self.recorder, math, float, '__ceil__'))

    def test_float_divmod(self):
        with RecodingActivated():
            x = 1.0
            divmod(x, 2.0)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__divmod__'))

    def test_float_eq(self):
        with RecodingActivated():
            x = 1.0
            x == 1.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__eq__'))

    @unittest.skip
    def test_float_float(self):
        with RecodingActivated():
            x = 1.0
            float(x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__float__'))

    @unittest.skip('float.__int__ is used instead')
    def test_float_floor(self):
        with RecodingActivated():
            x = 1.2
            math.floor(x)
        self.assertTrue(is_recorded(self.recorder, math, float, '__floor__'))

    def test_float_floordiv(self):
        with RecodingActivated():
            x = 1.0
            x // 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__floordiv__'))

    def test_float_ge(self):
        with RecodingActivated():
            x = 1.0
            x >= 1.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__ge__'))

    def test_float_gt(self):
        with RecodingActivated():
            x = 1.0
            x > 0.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__gt__'))

    @unittest.skip
    def test_float_hash(self):
        with RecodingActivated():
            x = 1.0
            hash(x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__hash__'))

    def test_float_int(self):
        with RecodingActivated():
            x = 1.0
            int(x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__int__'))

    def test_float_le(self):
        with RecodingActivated():
            x = 1.0
            x <= 1.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__le__'))

    def test_float_lt(self):
        with RecodingActivated():
            x = 1.0
            x < 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__lt__'))

    def test_float_mod(self):
        with RecodingActivated():
            x = 1.0
            x % 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__mod__'))

    def test_float_mul(self):
        with RecodingActivated():
            x = 1.0
            x * 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__mul__'))

    def test_float_ne(self):
        with RecodingActivated():
            x = 1.0
            x != 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__ne__'))

    def test_float_neg(self):
        with RecodingActivated():
            x = 1.0
            -x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__neg__'))

    def test_float_pos(self):
        with RecodingActivated():
            x = 1.0
            +x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__pos__'))

    def test_float_pow(self):
        with RecodingActivated():
            x = 2.0
            pow(x, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__pow__'))

    @unittest.skip('Recorded as non r method')
    def test_float_radd(self):
        with RecodingActivated():
            x = 1.0
            2.0 + x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__radd__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rdivmod(self):
        with RecodingActivated():
            x = 2.0
            divmod(4.0, x)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rdivmod__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rfloordiv(self):
        with RecodingActivated():
            x = 2.0
            4.0 // x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rfloordiv__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rmod(self):
        with RecodingActivated():
            x = 2.0
            4.0 % x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rmod__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rmul(self):
        with RecodingActivated():
            x = 2.0
            2.0 * x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rmul__'))

    def test_float_round(self):
        with RecodingActivated():
            x = 1.2345
            round(x, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__round__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rpow(self):
        with RecodingActivated():
            x = 2.0
            3.0**x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rpow__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rsub(self):
        with RecodingActivated():
            x = 1.0
            2.0 - x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rsub__'))

    @unittest.skip('Recorded as non r method')
    def test_float_rtruediv(self):
        with RecodingActivated():
            x = 2.0
            4.0 / x
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__rtruediv__'))

    def test_float_sub(self):
        with RecodingActivated():
            x = 1.0
            x - 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__sub__'))

    def test_float_truediv(self):
        with RecodingActivated():
            x = 1.0
            x / 2.0
        self.assertTrue(is_recorded(self.recorder, builtins, float, '__truediv__'))

    @unittest.skip('float.__int__ is used instead')
    def test_float_trunc(self):
        with RecodingActivated():
            x = 1.2345
            math.trunc(x)
        self.assertTrue(is_recorded(self.recorder, math, float, '__trunc__'))

    # Non-dunder methods
    def test_float_as_integer_ratio(self):
        with RecodingActivated():
            x = 1.0
            x.as_integer_ratio()
        self.assertTrue(is_recorded(self.recorder, builtins, float, 'as_integer_ratio'))

    def test_float_conjugate(self):
        with RecodingActivated():
            x = 1.0
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, builtins, float, 'conjugate'))

    def test_float_fromhex(self):
        with RecodingActivated():
            float.fromhex('0x1.ffffp10')
        self.assertTrue(is_recorded(self.recorder, builtins, float, 'fromhex'))

    def test_float_hex(self):
        with RecodingActivated():
            x = 1.0
            x.hex()
        self.assertTrue(is_recorded(self.recorder, builtins, float, 'hex'))

    def test_float_is_integer(self):
        with RecodingActivated():
            x = 1.0
            x.is_integer()
        self.assertTrue(is_recorded(self.recorder, builtins, float, 'is_integer'))
