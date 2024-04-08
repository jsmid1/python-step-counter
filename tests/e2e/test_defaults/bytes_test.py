import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded


class TestBytesMethods(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.module = sys.modules[__name__]
        self.recorder, _ = setup_recording(self.module, {sys, unittest, sr})

    @classmethod
    def tearDownClass(self):
        pass

    def tearDown(self):
        self.recorder.clear_data()

    def test_bytes_add(self):
        with recording_activated():
            x = b'Hello '
            x = x + b'World'
        self.assertTrue(is_recorded(self.recorder, bytes, '__add__'))

    def test_bytes_contains(self):
        with recording_activated():
            x = b'Hello '
            result = b'o' in x
        self.assertTrue(is_recorded(self.recorder, bytes, '__contains__'))

    def test_bytes_decode(self):
        with recording_activated():
            x = b'Hello '
            x = x.decode()
        self.assertTrue(is_recorded(self.recorder, bytes, 'decode'))

    def test_bytes_endswith(self):
        with recording_activated():
            x = b'Hello World'
            result = x.endswith(b'World')
        self.assertTrue(is_recorded(self.recorder, bytes, 'endswith'))

    def test_bytes_expandtabs(self):
        with recording_activated():
            x = b'Hello\tWorld'
            x = x.expandtabs()
        self.assertTrue(is_recorded(self.recorder, bytes, 'expandtabs'))

    def test_bytes_find(self):
        with recording_activated():
            x = b'Hello World'
            position = x.find(b'o')
        self.assertTrue(is_recorded(self.recorder, bytes, 'find'))

    def test_bytes_fromhex(self):
        with recording_activated():
            x = bytes.fromhex('48656c6c6f')
        self.assertTrue(is_recorded(self.recorder, bytes, 'fromhex'))

    def test_bytes_hex(self):
        with recording_activated():
            x = b'Hello'
            result = x.hex()
        self.assertTrue(is_recorded(self.recorder, bytes, 'hex'))

    def test_bytes_index(self):
        with recording_activated():
            x = b'Hello World'
            position = x.index(b'o')
        self.assertTrue(is_recorded(self.recorder, bytes, 'index'))

    def test_bytes_isalnum(self):
        with recording_activated():
            x = b'Hello123'
            result = x.isalnum()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isalnum'))

    def test_bytes_isalpha(self):
        with recording_activated():
            x = b'Hello'
            result = x.isalpha()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isalpha'))

    def test_bytes_isascii(self):
        with recording_activated():
            x = b'Hello'
            result = x.isascii()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isascii'))

    def test_bytes_isdigit(self):
        with recording_activated():
            x = b'123'
            result = x.isdigit()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isdigit'))

    def test_bytes_islower(self):
        with recording_activated():
            x = b'hello'
            result = x.islower()
        self.assertTrue(is_recorded(self.recorder, bytes, 'islower'))

    def test_bytes_isspace(self):
        with recording_activated():
            x = b' '
            result = x.isspace()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isspace'))

    def test_bytes_istitle(self):
        with recording_activated():
            x = b'Hello World'
            result = x.istitle()
        self.assertTrue(is_recorded(self.recorder, bytes, 'istitle'))

    def test_bytes_isupper(self):
        with recording_activated():
            x = b'HELLO'
            result = x.isupper()
        self.assertTrue(is_recorded(self.recorder, bytes, 'isupper'))

    def test_bytes_join(self):
        with recording_activated():
            x = b', '
            result = x.join([b'Hello', b'World'])
        self.assertTrue(is_recorded(self.recorder, bytes, 'join'))

    def test_bytes_ljust(self):
        with recording_activated():
            x = b'Hello'
            result = x.ljust(10)
        self.assertTrue(is_recorded(self.recorder, bytes, 'ljust'))

    def test_bytes_lower(self):
        with recording_activated():
            x = b'HELLO'
            result = x.lower()
        self.assertTrue(is_recorded(self.recorder, bytes, 'lower'))

    def test_bytes_lstrip(self):
        with recording_activated():
            x = b'  Hello'
            result = x.lstrip()
        self.assertTrue(is_recorded(self.recorder, bytes, 'lstrip'))

    def test_bytes_maketrans(self):
        with recording_activated():
            transtable = bytes.maketrans(b'lo', b'OL')
            x = b'hello world'.translate(transtable)
        self.assertTrue(is_recorded(self.recorder, bytes, 'maketrans'))

    def test_bytes_partition(self):
        with recording_activated():
            x = b'Hello World'
            result = x.partition(b' ')
        self.assertTrue(is_recorded(self.recorder, bytes, 'partition'))

    def test_bytes_removeprefix(self):
        with recording_activated():
            x = b'Hello World'
            result = x.removeprefix(b'Hello ')
        self.assertTrue(is_recorded(self.recorder, bytes, 'removeprefix'))

    def test_bytes_removesuffix(self):
        with recording_activated():
            x = b'Hello World'
            result = x.removesuffix(b' World')
        self.assertTrue(is_recorded(self.recorder, bytes, 'removesuffix'))

    def test_bytes_replace(self):
        with recording_activated():
            x = b'Hello World'
            result = x.replace(b'World', b'Universe')
        self.assertTrue(is_recorded(self.recorder, bytes, 'replace'))

    def test_bytes_rfind(self):
        with recording_activated():
            x = b'Hello World World'
            position = x.rfind(b'World')
        self.assertTrue(is_recorded(self.recorder, bytes, 'rfind'))

    def test_bytes_rindex(self):
        with recording_activated():
            x = b'Hello World World'
            position = x.rindex(b'World')
        self.assertTrue(is_recorded(self.recorder, bytes, 'rindex'))

    def test_bytes_rjust(self):
        with recording_activated():
            x = b'Hello'
            result = x.rjust(10)
        self.assertTrue(is_recorded(self.recorder, bytes, 'rjust'))

    def test_bytes_rpartition(self):
        with recording_activated():
            x = b'Hello World World'
            result = x.rpartition(b' ')
        self.assertTrue(is_recorded(self.recorder, bytes, 'rpartition'))

    def test_bytes_rsplit(self):
        with recording_activated():
            x = b'Hello World World'
            result = x.rsplit(b' ')
        self.assertTrue(is_recorded(self.recorder, bytes, 'rsplit'))

    def test_bytes_rstrip(self):
        with recording_activated():
            x = b'Hello World  '
            result = x.rstrip()
        self.assertTrue(is_recorded(self.recorder, bytes, 'rstrip'))

    def test_bytes_split(self):
        with recording_activated():
            x = b'Hello World'
            result = x.split(b' ')
        self.assertTrue(is_recorded(self.recorder, bytes, 'split'))

    def test_bytes_splitlines(self):
        with recording_activated():
            x = b'Hello\nWorld'
            result = x.splitlines()
        self.assertTrue(is_recorded(self.recorder, bytes, 'splitlines'))

    def test_bytes_startswith(self):
        with recording_activated():
            x = b'Hello World'
            result = x.startswith(b'Hello')
        self.assertTrue(is_recorded(self.recorder, bytes, 'startswith'))

    def test_bytes_strip(self):
        with recording_activated():
            x = b'  Hello World  '
            result = x.strip()
        self.assertTrue(is_recorded(self.recorder, bytes, 'strip'))

    def test_bytes_swapcase(self):
        with recording_activated():
            x = b'Hello World'
            result = x.swapcase()
        self.assertTrue(is_recorded(self.recorder, bytes, 'swapcase'))

    def test_bytes_title(self):
        with recording_activated():
            x = b'hello world'
            result = x.title()
        self.assertTrue(is_recorded(self.recorder, bytes, 'title'))

    def test_bytes_translate(self):
        with recording_activated():
            transtable = bytes.maketrans(b'lo', b'OL')
            x = b'hello world'.translate(transtable)
        self.assertTrue(is_recorded(self.recorder, bytes, 'translate'))

    def test_bytes_upper(self):
        with recording_activated():
            x = b'hello'
            result = x.upper()
        self.assertTrue(is_recorded(self.recorder, bytes, 'upper'))

    def test_bytes_zfill(self):
        with recording_activated():
            x = b'42'
            result = x.zfill(5)
        self.assertTrue(is_recorded(self.recorder, bytes, 'zfill'))
