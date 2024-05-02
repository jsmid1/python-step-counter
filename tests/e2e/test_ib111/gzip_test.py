import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import gzip


class TestTurtleMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

        os.chdir('tests/test_files/')

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_gzip_open(self):
        with RecodingActivated():
            with gzip.open('test.gz', 'wt') as f:
                f.write('test')
        self.assertTrue(is_recorded(self.recorder, gzip, None, 'open'))
