import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded


class TestByteArrayMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bytearray_add(self):
        with recording_activated():
            x = bytearray(b'Hello ')
            x = x + bytearray(b'World')
        self.assertTrue(is_recorded(self.recorder, bytearray, '__add__'))

    def test_bytearray_contains(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = b'o' in x
        self.assertTrue(is_recorded(self.recorder, bytearray, '__contains__'))

    def test_bytearray_decode(self):
        with recording_activated():
            x = bytearray(b'Hello')
            x = x.decode()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'decode'))

    def test_bytearray_endswith(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.endswith(b'World')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'endswith'))

    def test_bytearray_expandtabs(self):
        with recording_activated():
            x = bytearray(b'Hello\tWorld')
            x = x.expandtabs()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'expandtabs'))

    def test_bytearray_find(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            position = x.find(b'o')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'find'))

    def test_bytearray_fromhex(self):
        with recording_activated():
            x = bytearray.fromhex('48656c6c6f')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'fromhex'))

    def test_bytearray_hex(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.hex()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'hex'))

    def test_bytearray_index(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            position = x.index(b'o')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'index'))

    def test_bytearray_isalnum(self):
        with recording_activated():
            x = bytearray(b'Hello123')
            result = x.isalnum()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isalnum'))

    def test_bytearray_isalpha(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.isalpha()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isalpha'))

    def test_bytearray_isascii(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.isascii()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isascii'))

    def test_bytearray_isdigit(self):
        with recording_activated():
            x = bytearray(b'123')
            result = x.isdigit()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isdigit'))

    def test_bytearray_islower(self):
        with recording_activated():
            x = bytearray(b'hello')
            result = x.islower()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'islower'))

    def test_bytearray_isspace(self):
        with recording_activated():
            x = bytearray(b' ')
            result = x.isspace()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isspace'))

    def test_bytearray_istitle(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.istitle()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'istitle'))

    def test_bytearray_isupper(self):
        with recording_activated():
            x = bytearray(b'HELLO')
            result = x.isupper()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'isupper'))

    def test_bytearray_join(self):
        with recording_activated():
            x = bytearray(b', ')
            result = x.join([bytearray(b'Hello'), bytearray(b'World')])
        self.assertTrue(is_recorded(self.recorder, bytearray, 'join'))

    def test_bytearray_ljust(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.ljust(10)
        self.assertTrue(is_recorded(self.recorder, bytearray, 'ljust'))

    def test_bytearray_lower(self):
        with recording_activated():
            x = bytearray(b'HELLO')
            result = x.lower()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'lower'))

    def test_bytearray_lstrip(self):
        with recording_activated():
            x = bytearray(b'  Hello')
            result = x.lstrip()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'lstrip'))

    def test_bytearray_maketrans(self):
        with recording_activated():
            transtable = bytearray.maketrans(b'lo', b'OL')
            x = bytearray(b'hello world').translate(transtable)
        self.assertTrue(is_recorded(self.recorder, bytearray, 'maketrans'))

    def test_bytearray_partition(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.partition(b' ')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'partition'))

    def test_bytearray_pop(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.pop()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'pop'))

    def test_bytearray_remove(self):
        with recording_activated():
            x = bytearray(b'Hello')
            x.remove(ord('e'))
        self.assertTrue(is_recorded(self.recorder, bytearray, 'remove'))

    def test_bytearray_replace(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.replace(b'World', b'Universe')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'replace'))

    def test_bytearray_reverse(self):
        with recording_activated():
            x = bytearray(b'Hello')
            x.reverse()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'reverse'))

    def test_bytearray_rfind(self):
        with recording_activated():
            x = bytearray(b'Hello World World')
            position = x.rfind(b'World')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rfind'))

    def test_bytearray_rindex(self):
        with recording_activated():
            x = bytearray(b'Hello World World')
            position = x.rindex(b'World')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rindex'))

    def test_bytearray_rjust(self):
        with recording_activated():
            x = bytearray(b'Hello')
            result = x.rjust(10)
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rjust'))

    def test_bytearray_rpartition(self):
        with recording_activated():
            x = bytearray(b'Hello World World')
            result = x.rpartition(b' ')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rpartition'))

    def test_bytearray_rsplit(self):
        with recording_activated():
            x = bytearray(b'Hello World World')
            result = x.rsplit(b' ')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rsplit'))

    def test_bytearray_rstrip(self):
        with recording_activated():
            x = bytearray(b'Hello World  ')
            result = x.rstrip()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'rstrip'))

    def test_bytearray_split(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.split(b' ')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'split'))

    def test_bytearray_splitlines(self):
        with recording_activated():
            x = bytearray(b'Hello\nWorld')
            result = x.splitlines()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'splitlines'))

    def test_bytearray_startswith(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.startswith(b'Hello')
        self.assertTrue(is_recorded(self.recorder, bytearray, 'startswith'))

    def test_bytearray_strip(self):
        with recording_activated():
            x = bytearray(b'  Hello World  ')
            result = x.strip()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'strip'))

    def test_bytearray_swapcase(self):
        with recording_activated():
            x = bytearray(b'Hello World')
            result = x.swapcase()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'swapcase'))

    def test_bytearray_title(self):
        with recording_activated():
            x = bytearray(b'hello world')
            result = x.title()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'title'))

    def test_bytearray_translate(self):
        with recording_activated():
            transtable = bytearray.maketrans(b'lo', b'OL')
            x = bytearray(b'hello world').translate(transtable)
        self.assertTrue(is_recorded(self.recorder, bytearray, 'translate'))

    def test_bytearray_upper(self):
        with recording_activated():
            x = bytearray(b'hello')
            result = x.upper()
        self.assertTrue(is_recorded(self.recorder, bytearray, 'upper'))

    def test_bytearray_zfill(self):
        with recording_activated():
            x = bytearray(b'42')
            result = x.zfill(5)
        self.assertTrue(is_recorded(self.recorder, bytearray, 'zfill'))
