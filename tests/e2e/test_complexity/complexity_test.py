import math
import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import builtins


class TestCalendarMethods(unittest.TestCase):
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

    def test_list_getitem_complexity(self):
        list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        with RecodingActivated():
            list_[0]
        self.assertTrue(
            is_recorded(self.recorder, builtins, list, '__getitem__')
            and self.recorder.evaluate_data() == 1
        )

    def test_list_count_complexity(self):
        list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        length = len(list_)
        with RecodingActivated():
            list_.count(0)
        self.assertTrue(
            is_recorded(self.recorder, builtins, list, 'count')
            and self.recorder.evaluate_data() == length
        )

    def test_list_sort_complexity(self):
        list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        length = len(list_)
        with RecodingActivated():
            list_.sort()
        self.assertTrue(
            is_recorded(self.recorder, builtins, list, 'sort')
            and self.recorder.evaluate_data() == int(length * math.log(length, 2))
        )
