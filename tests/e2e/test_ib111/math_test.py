import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import math


class TestMathMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(None, self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_math_acos(self):
        with RecodingActivated():
            result = math.acos(0.5)
        self.assertTrue(is_recorded(self.recorder, math, None, 'acos'))

    def test_math_cos(self):
        with RecodingActivated():
            result = math.cos(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, None, 'cos'))

    def test_math_asin(self):
        with RecodingActivated():
            result = math.asin(0.5)
        self.assertTrue(is_recorded(self.recorder, math, None, 'asin'))

    def test_math_sin(self):
        with RecodingActivated():
            result = math.sin(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, None, 'sin'))

    def test_math_atan(self):
        with RecodingActivated():
            result = math.atan(1)
        self.assertTrue(is_recorded(self.recorder, math, None, 'atan'))

    def test_math_atan2(self):
        with RecodingActivated():
            result = math.atan2(1, 1)
        self.assertTrue(is_recorded(self.recorder, math, None, 'atan2'))

    def test_math_tan(self):
        with RecodingActivated():
            result = math.tan(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, None, 'tan'))

    def test_math_sqrt(self):
        with RecodingActivated():
            result = math.sqrt(4)
        self.assertTrue(is_recorded(self.recorder, math, None, 'sqrt'))

    def test_math_isqrt(self):
        with RecodingActivated():
            result = math.isqrt(4)
        self.assertTrue(is_recorded(self.recorder, math, None, 'isqrt'))

    def test_math_degrees(self):
        with RecodingActivated():
            result = math.degrees(math.pi)
        self.assertTrue(is_recorded(self.recorder, math, None, 'degrees'))

    def test_math_radians(self):
        with RecodingActivated():
            result = math.radians(180)
        self.assertTrue(is_recorded(self.recorder, math, None, 'radians'))

    def test_math_trunc(self):
        with RecodingActivated():
            result = math.trunc(3.14)
        self.assertTrue(is_recorded(self.recorder, math, None, 'trunc'))

    def test_math_floor(self):
        with RecodingActivated():
            result = math.floor(3.14)
        self.assertTrue(is_recorded(self.recorder, math, None, 'floor'))

    def test_math_ceil(self):
        with RecodingActivated():
            result = math.ceil(3.14)
        self.assertTrue(is_recorded(self.recorder, math, None, 'ceil'))

    def test_math_isclose(self):
        with RecodingActivated():
            result = math.isclose(1.1, 1.1000001)
        self.assertTrue(is_recorded(self.recorder, math, None, 'isclose'))

    def test_math_gcd(self):
        with RecodingActivated():
            result = math.gcd(36, 60)
        self.assertTrue(is_recorded(self.recorder, math, None, 'gcd'))

    def test_math_lcm(self):
        with RecodingActivated():
            result = math.lcm(12, 15)
        self.assertTrue(is_recorded(self.recorder, math, None, 'lcm'))

    def test_math_factorial(self):
        with RecodingActivated():
            result = math.factorial(5)
        self.assertTrue(is_recorded(self.recorder, math, None, 'factorial'))
