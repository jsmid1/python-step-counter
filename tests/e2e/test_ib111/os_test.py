import sys
import unittest
import os

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded


class TestOsMethods(unittest.TestCase):
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

    def test_os_remove(self):
        test_file = 'tetsfile.txt'
        with open(test_file, 'w') as _:
            pass
        with RecodingActivated():
            os.remove(test_file)
        self.assertTrue(is_recorded(self.recorder, os, None, 'remove'))

    def test_os_getcwd(self):
        with RecodingActivated():
            os.getcwd()
        self.assertTrue(is_recorded(self.recorder, os, None, 'getcwd'))

    def test_os_mkdir(self):
        test_dir = 'test_dir'
        with RecodingActivated():
            os.mkdir(test_dir)
        os.rmdir(test_dir)
        self.assertTrue(is_recorded(self.recorder, os, None, 'mkdir'))

    def test_os_listdir(self):
        with RecodingActivated():
            os.listdir('.')
        self.assertTrue(is_recorded(self.recorder, os, None, 'listdir'))

    def test_os_makedirs(self):
        dir_path = 'newdir/nesteddir'
        with RecodingActivated():
            os.makedirs(dir_path)
        self.assertTrue(is_recorded(self.recorder, os, None, 'makedirs'))
        os.removedirs(dir_path)

    def test_os_chdir(self):
        with RecodingActivated():
            os.chdir('.')
        self.assertTrue(is_recorded(self.recorder, os, None, 'chdir'))

    def test_os_scandir(self):
        with RecodingActivated():
            with os.scandir('.') as _:
                pass
        self.assertTrue(is_recorded(self.recorder, os, None, 'scandir'))

    def test_os_rmdir(self):
        os.mkdir('test_dir')
        with RecodingActivated():
            os.rmdir('test_dir')
        self.assertTrue(is_recorded(self.recorder, os, None, 'rmdir'))

    def test_os_rename(self):
        old_name = 'oldname'
        new_name = 'newname'
        with RecodingActivated():
            os.rename(old_name, new_name)
        os.rename(new_name, old_name)

        self.assertTrue(is_recorded(self.recorder, os, None, 'rename'))
