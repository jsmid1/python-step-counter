import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded
import builtins


class TestMemoryviewMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_memoryview_cast(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x.cast('B')
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'cast'))

    def test_memoryview_hex(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x.hex()
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'hex'))

    def test_memoryview_tobytes(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x.tobytes()
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'tobytes'))

    def test_memoryview_tolist(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x.tolist()
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'tolist'))

    def test_memoryview_release(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x.release()
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'release'))

    def test_memoryview_len(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            len(x)
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, '__len__'))

    def test_memoryview_getitem(self):
        with recording_activated():
            x = memoryview(b'Hello World')
            x[0]
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, '__getitem__'))

    @unittest.skip('Not recorder')
    def test_memoryview_setitem(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            view = memoryview(x)
            view[0] = ord('h')
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, '__setitem__'))

    def test_memoryview_toreadonly(self):
        with recording_activated():
            x = memoryview(bytearray(b'Hello World'))
            x.toreadonly()
        self.assertTrue(is_recorded(self.recorder, builtins, memoryview, 'toreadonly'))
