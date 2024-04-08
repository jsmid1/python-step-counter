import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

import re


class TestTurtleMethods(unittest.TestCase):
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

    def test_re_findall(self):
        with recording_activated():
            result = re.findall('a', 'aardvark')
        self.assertTrue(is_recorded(self.recorder, re, 'findall'))

    def test_re_match(self):
        with recording_activated():
            result = re.match('a', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, 'match'))

    def test_re_compile(self):
        with recording_activated():
            pattern = re.compile('a')
        self.assertTrue(is_recorded(self.recorder, re, 'compile'))

    def test_re_sub(self):
        with recording_activated():
            result = re.sub('a', 'o', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, 'sub'))

    def test_re_search(self):
        with recording_activated():
            result = re.search('a', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, 'search'))
