import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded
import builtins


class TestBytesMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, 'DETAIL', {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bytes_add(self):
        with RecodingActivated():
            x = b'Hello '
            x = x + b'World'
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, '__add__'))

    def test_bytes_contains(self):
        with RecodingActivated():
            x = b'Hello '
            result = b'o' in x
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, '__contains__'))

    def test_bytes_decode(self):
        with RecodingActivated():
            x = b'Hello '
            x = x.decode()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'decode'))

    def test_bytes_endswith(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.endswith(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'endswith'))

    def test_bytes_expandtabs(self):
        with RecodingActivated():
            x = b'Hello\tWorld'
            x = x.expandtabs()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'expandtabs'))

    def test_bytes_find(self):
        with RecodingActivated():
            x = b'Hello World'
            position = x.find(b'o')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'find'))

    def test_bytes_fromhex(self):
        with RecodingActivated():
            x = bytes.fromhex('48656c6c6f')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'fromhex'))

    def test_bytes_hex(self):
        with RecodingActivated():
            x = b'Hello'
            result = x.hex()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'hex'))

    def test_bytes_index(self):
        with RecodingActivated():
            x = b'Hello World'
            position = x.index(b'o')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'index'))

    def test_bytes_isalnum(self):
        with RecodingActivated():
            x = b'Hello123'
            result = x.isalnum()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isalnum'))

    def test_bytes_isalpha(self):
        with RecodingActivated():
            x = b'Hello'
            result = x.isalpha()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isalpha'))

    def test_bytes_isascii(self):
        with RecodingActivated():
            x = b'Hello'
            result = x.isascii()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isascii'))

    def test_bytes_isdigit(self):
        with RecodingActivated():
            x = b'123'
            result = x.isdigit()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isdigit'))

    def test_bytes_islower(self):
        with RecodingActivated():
            x = b'hello'
            result = x.islower()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'islower'))

    def test_bytes_isspace(self):
        with RecodingActivated():
            x = b' '
            result = x.isspace()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isspace'))

    def test_bytes_istitle(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.istitle()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'istitle'))

    def test_bytes_isupper(self):
        with RecodingActivated():
            x = b'HELLO'
            result = x.isupper()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'isupper'))

    def test_bytes_join(self):
        with RecodingActivated():
            x = b', '
            result = x.join([b'Hello', b'World'])
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'join'))

    def test_bytes_ljust(self):
        with RecodingActivated():
            x = b'Hello'
            result = x.ljust(10)
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'ljust'))

    def test_bytes_lower(self):
        with RecodingActivated():
            x = b'HELLO'
            result = x.lower()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'lower'))

    def test_bytes_lstrip(self):
        with RecodingActivated():
            x = b'  Hello'
            result = x.lstrip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'lstrip'))

    def test_bytes_maketrans(self):
        with RecodingActivated():
            transtable = bytes.maketrans(b'lo', b'OL')
            x = b'hello world'.translate(transtable)
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'maketrans'))

    def test_bytes_partition(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.partition(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'partition'))

    def test_bytes_removeprefix(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.removeprefix(b'Hello ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'removeprefix'))

    def test_bytes_removesuffix(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.removesuffix(b' World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'removesuffix'))

    def test_bytes_replace(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.replace(b'World', b'Universe')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'replace'))

    def test_bytes_rfind(self):
        with RecodingActivated():
            x = b'Hello World World'
            position = x.rfind(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rfind'))

    def test_bytes_rindex(self):
        with RecodingActivated():
            x = b'Hello World World'
            position = x.rindex(b'World')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rindex'))

    def test_bytes_rjust(self):
        with RecodingActivated():
            x = b'Hello'
            result = x.rjust(10)
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rjust'))

    def test_bytes_rpartition(self):
        with RecodingActivated():
            x = b'Hello World World'
            result = x.rpartition(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rpartition'))

    def test_bytes_rsplit(self):
        with RecodingActivated():
            x = b'Hello World World'
            result = x.rsplit(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rsplit'))

    def test_bytes_rstrip(self):
        with RecodingActivated():
            x = b'Hello World  '
            result = x.rstrip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'rstrip'))

    def test_bytes_split(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.split(b' ')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'split'))

    def test_bytes_splitlines(self):
        with RecodingActivated():
            x = b'Hello\nWorld'
            result = x.splitlines()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'splitlines'))

    def test_bytes_startswith(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.startswith(b'Hello')
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'startswith'))

    def test_bytes_strip(self):
        with RecodingActivated():
            x = b'  Hello World  '
            result = x.strip()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'strip'))

    def test_bytes_swapcase(self):
        with RecodingActivated():
            x = b'Hello World'
            result = x.swapcase()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'swapcase'))

    def test_bytes_title(self):
        with RecodingActivated():
            x = b'hello world'
            result = x.title()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'title'))

    def test_bytes_translate(self):
        with RecodingActivated():
            transtable = bytes.maketrans(b'lo', b'OL')
            x = b'hello world'.translate(transtable)
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'translate'))

    def test_bytes_upper(self):
        with RecodingActivated():
            x = b'hello'
            result = x.upper()
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'upper'))

    def test_bytes_zfill(self):
        with RecodingActivated():
            x = b'42'
            result = x.zfill(5)
        self.assertTrue(is_recorded(self.recorder, builtins, bytes, 'zfill'))
