import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded


class TestTurtleMethods(unittest.TestCase):
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

    @unittest.skip('Requires input')
    def test_sys_stdin(self):
        with RecodingActivated():
            input = sys.stdin.readline()
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stdin'))

    @unittest.skip('stdout')
    def test_sys_stdout(self):
        with RecodingActivated():
            sys.stdout.write('test')
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stdout'))

    @unittest.skip('stderr')
    def test_sys_stderr(self):
        with RecodingActivated():
            sys.stderr.write('error')
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stderr'))
