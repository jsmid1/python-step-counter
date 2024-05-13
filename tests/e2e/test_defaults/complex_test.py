import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestComplexMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_complex_abs(self):
        with RecodingActivated():
            x = complex(-1, 1)
            abs(x)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__abs__'))

    def test_complex_add(self):
        with RecodingActivated():
            x = complex(1, 1)
            x + complex(1, -1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__add__'))

    def test_complex_bool(self):
        with RecodingActivated():
            x = complex(0, 0)
            bool(x)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__bool__'))

    def test_complex_eq(self):
        with RecodingActivated():
            x = complex(1, 1)
            x == complex(1, 1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__eq__'))

    def test_complex_ge(self):
        with RecodingActivated():
            try:
                x = complex(1, 1)
                x >= complex(1, 0)
            except TypeError:
                pass
        self.assertTrue(
            is_recorded(self.recorder, builtins, complex, '__ge__'),
            'Complex does not support ordering',
        )

    def test_complex_gt(self):
        with RecodingActivated():
            try:
                x = complex(1, 1)
                x > complex(0, 1)
            except TypeError:
                pass
        self.assertTrue(
            is_recorded(self.recorder, builtins, complex, '__gt__'),
            'Complex does not support ordering',
        )

    def test_complex_le(self):
        with RecodingActivated():
            try:
                x = complex(1, 1)
                x <= complex(1, 0)
            except TypeError:
                pass
        self.assertTrue(
            is_recorded(self.recorder, builtins, complex, '__le__'),
            'Complex does not support ordering',
        )

    def test_complex_lt(self):
        with RecodingActivated():
            try:
                x = complex(1, 1)
                x < complex(2, 1)
            except TypeError:
                pass
        self.assertTrue(
            is_recorded(self.recorder, builtins, complex, '__lt__'),
            'Complex does not support ordering',
        )

    def test_complex_mul(self):
        with RecodingActivated():
            x = complex(1, 1)
            x * complex(1, -1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__mul__'))

    def test_complex_ne(self):
        with RecodingActivated():
            x = complex(1, 1)
            x != complex(1, -1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__ne__'))

    def test_complex_neg(self):
        with RecodingActivated():
            x = complex(1, 1)
            -x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__neg__'))

    def test_complex_pos(self):
        with RecodingActivated():
            x = complex(1, 1)
            +x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__pos__'))

    def test_complex_pow(self):
        with RecodingActivated():
            x = complex(1, 1)
            pow(x, 2)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__pow__'))

    @unittest.skip
    def test_complex_radd(self):
        with RecodingActivated():
            x = complex(1, 1)
            1 + x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__radd__'))

    @unittest.skip
    def test_complex_rmul(self):
        with RecodingActivated():
            x = complex(1, 1)
            2 * x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__rmul__'))

    @unittest.skip
    def test_complex_rpow(self):
        with RecodingActivated():
            x = complex(1, 1)
            2**x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__rpow__'))

    @unittest.skip
    def test_complex_rsub(self):
        with RecodingActivated():
            x = complex(1, 1)
            1 - x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__rsub__'))

    @unittest.skip
    def test_complex_rtruediv(self):
        with RecodingActivated():
            x = complex(1, 1)
            1 / x
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__rtruediv__'))

    def test_complex_sub(self):
        with RecodingActivated():
            x = complex(1, 1)
            x - complex(1, -1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__sub__'))

    def test_complex_truediv(self):
        with RecodingActivated():
            x = complex(1, 1)
            x / complex(1, -1)
        self.assertTrue(is_recorded(self.recorder, builtins, complex, '__truediv__'))

    # Non-dunder methods
    def test_complex_conjugate(self):
        with RecodingActivated():
            x = complex(1, -1)
            x.conjugate()
        self.assertTrue(is_recorded(self.recorder, builtins, complex, 'conjugate'))
