import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import math
import operator
import builtins


class TestIntMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_int_abs(self):
        with RecodingActivated():
            x = -1
            abs(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__abs__'))

    def test_int_add(self):
        with RecodingActivated():
            x = 1
            x + 1
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__add__'))

    def test_int_and(self):
        with RecodingActivated():
            x = 1
            x & 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__and__'))

    def test_int_bool(self):
        with RecodingActivated():
            x = 1
            bool(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__bool__'))

    @unittest.skip("Records as math module function")
    def test_int_ceil(self):
        with RecodingActivated():
            x = 1
            math.ceil(x)
        self.assertTrue(is_recorded(self.recorder, math, None, '__ceil__'))

    # Skipping methods like __class__, __delattr__, __dir__, __doc__ as they do not fit the operational testing pattern

    def test_int_divmod(self):
        with RecodingActivated():
            x = 1
            divmod(x, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__divmod__'))

    def test_int_eq(self):
        with RecodingActivated():
            x = 1
            x == 1
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__eq__'))

    def test_int_float(self):
        with RecodingActivated():
            x = 1
            float(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__float__'))

    @unittest.skip("Records as math module function")
    def test_int_floor(self):
        with RecodingActivated():
            x = 1
            math.floor(x)
        self.assertTrue(is_recorded(self.recorder, math, None, '__floor__'))

    def test_int_floordiv(self):
        with RecodingActivated():
            x = 1
            x // 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__floordiv__'))

    @unittest.skip
    def test_int_format(self):
        with RecodingActivated():
            x = 1
            format(x, "b")
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__format__'))

    def test_int_ge(self):
        with RecodingActivated():
            x = 1
            x >= 1
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__ge__'))

    @unittest.skip
    def test_int_getattribute(self):
        with RecodingActivated():
            x = 1
            getattr(x, "__str__")  # Example use case
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__getattribute__'))

    # __getnewargs__ is typically not invoked directly in operational testing

    def test_int_gt(self):
        with RecodingActivated():
            x = 1
            x > 0
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__gt__'))

    @unittest.skip('Not recorder')
    def test_int_hash(self):
        with RecodingActivated():
            x = 1
            hash(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__hash__'))

    @unittest.skip(
        ' Would be recorded under operator module but import of operator is nor allowed'
    )
    def test_int_index(self):
        with RecodingActivated():
            x = 1
            operator.index(x)
        self.assertTrue(is_recorded(self.recorder, operator, None, 'index'))

    @unittest.skip
    def test_int_int(self):
        with RecodingActivated():
            x = 1
            int(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__int__'))

    def test_int_invert(self):
        with RecodingActivated():
            x = 1
            ~x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__invert__'))

    def test_int_le(self):
        with RecodingActivated():
            x = 1
            x <= 1
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__le__'))

    def test_int_lshift(self):
        with RecodingActivated():
            x = 1
            x << 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__lshift__'))

    def test_int_lt(self):
        with RecodingActivated():
            x = 1
            x < 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__lt__'))

    def test_int_mod(self):
        with RecodingActivated():
            x = 1
            x % 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__mod__'))

    def test_int_mul(self):
        with RecodingActivated():
            x = 1
            x * 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__mul__'))

    def test_int_ne(self):
        with RecodingActivated():
            x = 1
            x != 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__ne__'))

    def test_int_neg(self):
        with RecodingActivated():
            x = 1
            -x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__neg__'))

    def test_int_or(self):
        with RecodingActivated():
            x = 1
            x | 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__or__'))

    def test_int_pos(self):
        with RecodingActivated():
            x = 1
            +x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__pos__'))

    def test_int_pow(self):
        with RecodingActivated():
            x = 2
            pow(x, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__pow__'))

    @unittest.skip
    def test_int_radd(self):
        with RecodingActivated():
            x = 1
            1 + x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__radd__'))

    @unittest.skip
    def test_int_rand(self):
        with RecodingActivated():
            x = 1
            1 & x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rand__'))

    @unittest.skip
    def test_int_rdivmod(self):
        with RecodingActivated():
            x = 2
            divmod(4, x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rdivmod__'))

    @unittest.skip
    def test_int_rfloordiv(self):
        with RecodingActivated():
            x = 2
            4 // x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rfloordiv__'))

    @unittest.skip
    def test_int_rlshift(self):
        with RecodingActivated():
            x = 2
            1 << x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rlshift__'))

    @unittest.skip
    def test_int_rmod(self):
        with RecodingActivated():
            x = 2
            4 % x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rmod__'))

    @unittest.skip
    def test_int_rmul(self):
        with RecodingActivated():
            x = 2
            2 * x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rmul__'))

    @unittest.skip
    def test_int_ror(self):
        with RecodingActivated():
            x = 1
            2 | x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__ror__'))

    @unittest.skip
    def test_int_rpow(self):
        with RecodingActivated():
            x = 2
            3**x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rpow__'))

    @unittest.skip
    def test_int_rrshift(self):
        with RecodingActivated():
            x = 1
            2 >> x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rrshift__'))

    @unittest.skip
    def test_int_rshift(self):
        with RecodingActivated():
            x = 4
            x >> 1
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rshift__'))

    @unittest.skip
    def test_int_rsub(self):
        with RecodingActivated():
            x = 1
            2 - x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rsub__'))

    @unittest.skip
    def test_int_rtruediv(self):
        with RecodingActivated():
            x = 2
            4 / x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rtruediv__'))

    @unittest.skip
    def test_int_rxor(self):
        with RecodingActivated():
            x = 1
            3 ^ x
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__rxor__'))

    @unittest.skip
    def test_int_setattr(self):
        with RecodingActivated():
            x = 1
            setattr(x, 'dummy_attribute', 100)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__setattr__'))

    @unittest.skip
    def test_int_sizeof(self):
        with RecodingActivated():
            x = 1
            x.__sizeof__()
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__sizeof__'))

    def test_int_str(self):
        with RecodingActivated():
            x = 1
            str(x)
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__str__'))

    def test_int_sub(self):
        with RecodingActivated():
            x = 1
            x - 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__sub__'))

    def test_int_truediv(self):
        with RecodingActivated():
            x = 1
            x / 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__truediv__'))

    @unittest.skip("Records as math module function")
    def test_int_trunc(self):
        with RecodingActivated():
            x = 1
            math.trunc(x)
        self.assertTrue(is_recorded(self.recorder, math, None, '__trunc__'))

    def test_int_xor(self):
        with RecodingActivated():
            x = 1
            x ^ 2
        self.assertTrue(is_recorded(self.recorder, builtins, int, '__xor__'))

    def test_int_as_integer_ratio(self):
        with RecodingActivated():
            x = 1
            x.as_integer_ratio()
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'as_integer_ratio'))

    def test_int_bit_count(self):
        with RecodingActivated():
            x = 1
            x.bit_count()
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'bit_count'))

    def test_int_bit_length(self):
        with RecodingActivated():
            x = 1
            x.bit_length()
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'bit_length'))

    def test_int_conjugate(self):
        with RecodingActivated():
            x = 1
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'conjugate'))

    def test_int_from_bytes(self):
        with RecodingActivated():
            bytes_val = (1).to_bytes(1, byteorder='big')
            int.from_bytes(bytes_val, byteorder='big')
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'from_bytes'))

    def test_int_to_bytes(self):
        with RecodingActivated():
            x = 1
            x.to_bytes(1, byteorder='big')
        self.assertTrue(is_recorded(self.recorder, builtins, int, 'to_bytes'))


if __name__ == '__main__':
    unittest.main()
