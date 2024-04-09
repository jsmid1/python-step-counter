import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded


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

    @unittest.skip('Requires input')
    def test_sys_stdin(self):
        with recording_activated():
            input = sys.stdin.readline()
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stdin'))

    @unittest.skip('stdout')
    def test_sys_stdout(self):
        with recording_activated():
            sys.stdout.write('test')
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stdout'))

    @unittest.skip('stderr')
    def test_sys_stderr(self):
        with recording_activated():
            sys.stderr.write('error')
        self.assertTrue(is_recorded(self.recorder, sys, None, 'stderr'))
