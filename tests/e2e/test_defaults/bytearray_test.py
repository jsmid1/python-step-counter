import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestByteArrayMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(None, self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bytearray_add(self):
        x = bytearray(b'Hello ')
        with RecodingActivated():
            x = x + bytearray(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, '__add__'))

    def test_bytearray_contains(self):
        x = bytearray(b'Hello')
        with RecodingActivated():
            b'o' in x
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, '__contains__'))

    def test_bytearray_decode(self):
        x = bytearray(b'Hello')
        with RecodingActivated():
            x = x.decode()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'decode'))

    def test_bytearray_endswith(self):
        x = bytearray(b'Hello World')
        with RecodingActivated():
            x.endswith(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'endswith'))

    def test_bytearray_expandtabs(self):
        x = bytearray(b'Hello\tWorld')
        with RecodingActivated():
            x.expandtabs()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'expandtabs'))

    def test_bytearray_find(self):
        x = bytearray(b'Hello World')
        with RecodingActivated():
            x.find(b'o')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'find'))

    def test_bytearray_fromhex(self):
        with RecodingActivated():
            bytearray.fromhex('48656c6c6f')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'fromhex'))

    def test_bytearray_hex(self):
        x = bytearray(b'Hello')
        with RecodingActivated():
            x.hex()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'hex'))

    def test_bytearray_index(self):
        x = bytearray(b'Hello World')
        with RecodingActivated():
            x.index(b'o')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'index'))

    def test_bytearray_isalnum(self):
        with RecodingActivated():
            x = bytearray(b'Hello123')
            x.isalnum()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isalnum'))

    def test_bytearray_isalpha(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.isalpha()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isalpha'))

    def test_bytearray_isascii(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.isascii()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isascii'))

    def test_bytearray_isdigit(self):
        with RecodingActivated():
            x = bytearray(b'123')
            x.isdigit()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isdigit'))

    def test_bytearray_islower(self):
        with RecodingActivated():
            x = bytearray(b'hello')
            x.islower()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'islower'))

    def test_bytearray_isspace(self):
        with RecodingActivated():
            x = bytearray(b' ')
            x.isspace()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isspace'))

    def test_bytearray_istitle(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.istitle()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'istitle'))

    def test_bytearray_isupper(self):
        with RecodingActivated():
            x = bytearray(b'HELLO')
            x.isupper()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'isupper'))

    def test_bytearray_join(self):
        with RecodingActivated():
            x = bytearray(b', ')
            x.join([bytearray(b'Hello'), bytearray(b'World')])
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'join'))

    def test_bytearray_ljust(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.ljust(10)
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'ljust'))

    def test_bytearray_lower(self):
        with RecodingActivated():
            x = bytearray(b'HELLO')
            x.lower()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'lower'))

    def test_bytearray_lstrip(self):
        with RecodingActivated():
            x = bytearray(b'  Hello')
            x.lstrip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'lstrip'))

    def test_bytearray_maketrans(self):
        with RecodingActivated():
            transtable = bytearray.maketrans(b'lo', b'OL')
            x = bytearray(b'hello world').translate(transtable)
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'maketrans'))

    def test_bytearray_partition(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.partition(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'partition'))

    def test_bytearray_pop(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.pop()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'pop'))

    def test_bytearray_remove(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.remove(ord('e'))
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'remove'))

    def test_bytearray_replace(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.replace(b'World', b'Universe')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'replace'))

    def test_bytearray_reverse(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.reverse()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'reverse'))

    def test_bytearray_rfind(self):
        with RecodingActivated():
            x = bytearray(b'Hello World World')
            x.rfind(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rfind'))

    def test_bytearray_rindex(self):
        with RecodingActivated():
            x = bytearray(b'Hello World World')
            x.rindex(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rindex'))

    def test_bytearray_rjust(self):
        with RecodingActivated():
            x = bytearray(b'Hello')
            x.rjust(10)
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rjust'))

    def test_bytearray_rpartition(self):
        with RecodingActivated():
            x = bytearray(b'Hello World World')
            x.rpartition(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rpartition'))

    def test_bytearray_rsplit(self):
        with RecodingActivated():
            x = bytearray(b'Hello World World')
            x.rsplit(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rsplit'))

    def test_bytearray_rstrip(self):
        with RecodingActivated():
            x = bytearray(b'Hello World  ')
            x.rstrip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'rstrip'))

    def test_bytearray_split(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.split(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'split'))

    def test_bytearray_splitlines(self):
        with RecodingActivated():
            x = bytearray(b'Hello\nWorld')
            x.splitlines()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'splitlines'))

    def test_bytearray_startswith(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.startswith(b'Hello')
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'startswith'))

    def test_bytearray_strip(self):
        with RecodingActivated():
            x = bytearray(b'  Hello World  ')
            x.strip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'strip'))

    def test_bytearray_swapcase(self):
        with RecodingActivated():
            x = bytearray(b'Hello World')
            x.swapcase()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'swapcase'))

    def test_bytearray_title(self):
        with RecodingActivated():
            x = bytearray(b'hello world')
            x.title()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'title'))

    def test_bytearray_translate(self):
        transtable = bytearray.maketrans(b'lo', b'OL')
        with RecodingActivated():
            bytearray(b'hello world').translate(transtable)
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'translate'))

    def test_bytearray_upper(self):
        with RecodingActivated():
            x = bytearray(b'hello')
            x.upper()
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'upper'))

    def test_bytearray_zfill(self):
        with RecodingActivated():
            x = bytearray(b'42')
            x.zfill(5)
        self.assertTrue(is_recorded(self.recorder, builtins, bytearray, 'zfill'))
