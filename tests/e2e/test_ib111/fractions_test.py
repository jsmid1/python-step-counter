import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import fractions


class TestFractionMethods(unittest.TestCase):
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

    def test_Fraction_test(self):
        fraction = fractions.Fraction(1, 2)
        with recording_activated():
            fraction.from_float(5.5)
        self.assertTrue(is_recorded(self.recorder, fractions.Fraction, 'from_float'))
