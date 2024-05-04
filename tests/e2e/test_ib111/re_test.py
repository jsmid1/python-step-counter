import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import re


class TestReMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_re_findall(self):
        with RecodingActivated():
            result = re.findall('a', 'aardvark')
        self.assertTrue(is_recorded(self.recorder, re, None, 'findall'))

    def test_re_match(self):
        with RecodingActivated():
            result = re.match('a', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, None, 'match'))

    def test_re_compile(self):
        with RecodingActivated():
            pattern = re.compile('a')
        self.assertTrue(is_recorded(self.recorder, re, None, 'compile'))

    def test_re_sub(self):
        with RecodingActivated():
            result = re.sub('a', 'o', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, None, 'sub'))

    def test_re_search(self):
        with RecodingActivated():
            result = re.search('a', 'apple')
        self.assertTrue(is_recorded(self.recorder, re, None, 'search'))
