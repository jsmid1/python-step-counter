import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import math


class TestFloatMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_float_abs(self):
        with recording_activated():
            x = -1.0
            abs(x)
        self.assertTrue(is_recorded(self.recorder, float, '__abs__'))

    def test_float_add(self):
        with recording_activated():
            x = 1.0
            x + 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__add__'))

    def test_float_bool(self):
        with recording_activated():
            x = 1.0
            bool(x)
        self.assertTrue(is_recorded(self.recorder, float, '__bool__'))

    @unittest.skip('Never used')
    def test_float_ceil(self):
        with recording_activated():
            x = 1.2
            math.ceil(x)
        self.assertTrue(is_recorded(self.recorder, float, '__ceil__'))

    def test_float_divmod(self):
        with recording_activated():
            x = 1.0
            divmod(x, 2.0)
        self.assertTrue(is_recorded(self.recorder, float, '__divmod__'))

    def test_float_eq(self):
        with recording_activated():
            x = 1.0
            x == 1.0
        self.assertTrue(is_recorded(self.recorder, float, '__eq__'))

    @unittest.skip
    def test_float_float(self):
        with recording_activated():
            x = 1.0
            float(x)
        self.assertTrue(is_recorded(self.recorder, float, '__float__'))

    @unittest.skip('float.__int__ is used instead')
    def test_float_floor(self):
        with recording_activated():
            x = 1.2
            math.floor(x)
        self.assertTrue(is_recorded(self.recorder, float, '__floor__'))

    def test_float_floordiv(self):
        with recording_activated():
            x = 1.0
            x // 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__floordiv__'))

    def test_float_ge(self):
        with recording_activated():
            x = 1.0
            x >= 1.0
        self.assertTrue(is_recorded(self.recorder, float, '__ge__'))

    def test_float_gt(self):
        with recording_activated():
            x = 1.0
            x > 0.0
        self.assertTrue(is_recorded(self.recorder, float, '__gt__'))

    @unittest.skip
    def test_float_hash(self):
        with recording_activated():
            x = 1.0
            hash(x)
        self.assertTrue(is_recorded(self.recorder, float, '__hash__'))

    def test_float_int(self):
        with recording_activated():
            x = 1.0
            int(x)
        self.assertTrue(is_recorded(self.recorder, float, '__int__'))

    def test_float_le(self):
        with recording_activated():
            x = 1.0
            x <= 1.0
        self.assertTrue(is_recorded(self.recorder, float, '__le__'))

    def test_float_lt(self):
        with recording_activated():
            x = 1.0
            x < 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__lt__'))

    def test_float_mod(self):
        with recording_activated():
            x = 1.0
            x % 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__mod__'))

    def test_float_mul(self):
        with recording_activated():
            x = 1.0
            x * 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__mul__'))

    def test_float_ne(self):
        with recording_activated():
            x = 1.0
            x != 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__ne__'))

    def test_float_neg(self):
        with recording_activated():
            x = 1.0
            -x
        self.assertTrue(is_recorded(self.recorder, float, '__neg__'))

    def test_float_pos(self):
        with recording_activated():
            x = 1.0
            +x
        self.assertTrue(is_recorded(self.recorder, float, '__pos__'))

    def test_float_pow(self):
        with recording_activated():
            x = 2.0
            pow(x, 2)
        self.assertTrue(is_recorded(self.recorder, float, '__pow__'))

    @unittest.skip
    def test_float_radd(self):
        with recording_activated():
            x = 1.0
            2.0 + x
        self.assertTrue(is_recorded(self.recorder, float, '__radd__'))

    @unittest.skip
    def test_float_rdivmod(self):
        with recording_activated():
            x = 2.0
            divmod(4.0, x)
        self.assertTrue(is_recorded(self.recorder, float, '__rdivmod__'))

    @unittest.skip
    def test_float_rfloordiv(self):
        with recording_activated():
            x = 2.0
            4.0 // x
        self.assertTrue(is_recorded(self.recorder, float, '__rfloordiv__'))

    @unittest.skip
    def test_float_rmod(self):
        with recording_activated():
            x = 2.0
            4.0 % x
        self.assertTrue(is_recorded(self.recorder, float, '__rmod__'))

    @unittest.skip
    def test_float_rmul(self):
        with recording_activated():
            x = 2.0
            2.0 * x
        self.assertTrue(is_recorded(self.recorder, float, '__rmul__'))

    def test_float_round(self):
        with recording_activated():
            x = 1.2345
            round(x, 2)
        self.assertTrue(is_recorded(self.recorder, float, '__round__'))

    @unittest.skip
    def test_float_rpow(self):
        with recording_activated():
            x = 2.0
            3.0**x
        self.assertTrue(is_recorded(self.recorder, float, '__rpow__'))

    @unittest.skip
    def test_float_rsub(self):
        with recording_activated():
            x = 1.0
            2.0 - x
        self.assertTrue(is_recorded(self.recorder, float, '__rsub__'))

    @unittest.skip
    def test_float_rtruediv(self):
        with recording_activated():
            x = 2.0
            4.0 / x
        self.assertTrue(is_recorded(self.recorder, float, '__rtruediv__'))

    def test_float_sub(self):
        with recording_activated():
            x = 1.0
            x - 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__sub__'))

    def test_float_truediv(self):
        with recording_activated():
            x = 1.0
            x / 2.0
        self.assertTrue(is_recorded(self.recorder, float, '__truediv__'))

    @unittest.skip('float.__int__ is used instead')
    def test_float_trunc(self):
        with recording_activated():
            x = 1.2345
            math.trunc(x)
        self.assertTrue(is_recorded(self.recorder, float, '__trunc__'))

    # Non-dunder methods
    def test_float_as_integer_ratio(self):
        with recording_activated():
            x = 1.0
            x.as_integer_ratio()
        self.assertTrue(is_recorded(self.recorder, float, 'as_integer_ratio'))

    def test_float_conjugate(self):
        with recording_activated():
            x = 1.0
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, float, 'conjugate'))

    def test_float_fromhex(self):
        with recording_activated():
            float.fromhex('0x1.ffffp10')
        self.assertTrue(is_recorded(self.recorder, float, 'fromhex'))

    def test_float_hex(self):
        with recording_activated():
            x = 1.0
            x.hex()
        self.assertTrue(is_recorded(self.recorder, float, 'hex'))

    def test_float_is_integer(self):
        with recording_activated():
            x = 1.0
            x.is_integer()
        self.assertTrue(is_recorded(self.recorder, float, 'is_integer'))
