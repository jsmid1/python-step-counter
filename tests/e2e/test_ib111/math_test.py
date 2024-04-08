import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import math


class TestMathMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = sys.modules[__name__]
        cls.recorder, _ = setup_recording(cls.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_math_acos(self):
        with recording_activated():
            result = math.acos(0.5)
        self.assertTrue(is_recorded(self.recorder, math, 'acos'))

    def test_math_cos(self):
        with recording_activated():
            result = math.cos(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, 'cos'))

    def test_math_asin(self):
        with recording_activated():
            result = math.asin(0.5)
        self.assertTrue(is_recorded(self.recorder, math, 'asin'))

    def test_math_sin(self):
        with recording_activated():
            result = math.sin(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, 'sin'))

    def test_math_atan(self):
        with recording_activated():
            result = math.atan(1)
        self.assertTrue(is_recorded(self.recorder, math, 'atan'))

    def test_math_atan2(self):
        with recording_activated():
            result = math.atan2(1, 1)
        self.assertTrue(is_recorded(self.recorder, math, 'atan2'))

    def test_math_tan(self):
        with recording_activated():
            result = math.tan(math.pi / 4)
        self.assertTrue(is_recorded(self.recorder, math, 'tan'))

    def test_math_sqrt(self):
        with recording_activated():
            result = math.sqrt(4)
        self.assertTrue(is_recorded(self.recorder, math, 'sqrt'))

    def test_math_isqrt(self):
        with recording_activated():
            result = math.isqrt(4)
        self.assertTrue(is_recorded(self.recorder, math, 'isqrt'))

    def test_math_degrees(self):
        with recording_activated():
            result = math.degrees(math.pi)
        self.assertTrue(is_recorded(self.recorder, math, 'degrees'))

    def test_math_radians(self):
        with recording_activated():
            result = math.radians(180)
        self.assertTrue(is_recorded(self.recorder, math, 'radians'))

    def test_math_trunc(self):
        with recording_activated():
            result = math.trunc(3.14)
        self.assertTrue(is_recorded(self.recorder, math, 'trunc'))

    def test_math_floor(self):
        with recording_activated():
            result = math.floor(3.14)
        self.assertTrue(is_recorded(self.recorder, math, 'floor'))

    def test_math_ceil(self):
        with recording_activated():
            result = math.ceil(3.14)
        self.assertTrue(is_recorded(self.recorder, math, 'ceil'))

    def test_math_isclose(self):
        with recording_activated():
            result = math.isclose(1.1, 1.1000001)
        self.assertTrue(is_recorded(self.recorder, math, 'isclose'))

    def test_math_gcd(self):
        with recording_activated():
            result = math.gcd(36, 60)
        self.assertTrue(is_recorded(self.recorder, math, 'gcd'))

    def test_math_lcm(self):
        with recording_activated():
            result = math.lcm(12, 15)
        self.assertTrue(is_recorded(self.recorder, math, 'lcm'))

    def test_math_factorial(self):
        with recording_activated():
            result = math.factorial(5)
        self.assertTrue(is_recorded(self.recorder, math, 'factorial'))
