import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import shutil


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

    def test_shutil_rmtree(self):
        testdir = 'testdir'
        os.mkdir(testdir)
        with RecodingActivated():
            shutil.rmtree(testdir)
        self.assertTrue(is_recorded(self.recorder, shutil, None, 'rmtree'))

    def test_shutil_copyfile(self):
        test_file = 'test.txt'
        cp_file = 'dest.txt'
        try:
            with open(test_file, 'w') as _:
                pass
            os.remove(cp_file)
        except:
            pass
        with RecodingActivated():
            shutil.copyfile(test_file, cp_file)
        self.assertTrue(is_recorded(self.recorder, shutil, None, 'copyfile'))
