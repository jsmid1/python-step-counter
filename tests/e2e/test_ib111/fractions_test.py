import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import fractions


class TestFractionMethods(unittest.TestCase):
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

    def test_Fraction_test(self):
        fraction = fractions.Fraction(1, 2)
        with RecodingActivated():
            fraction.from_float(5.5)
        self.assertTrue(
            is_recorded(self.recorder, fractions, fractions.Fraction, 'from_float')
        )
