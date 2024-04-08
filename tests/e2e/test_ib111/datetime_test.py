import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, recording_activated

from ..utils import is_recorded

from datetime import date, datetime, time, timedelta


class TestDatetimeMethods(unittest.TestCase):
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

    def test_date_today_test(self):
        d = date(1, 2, 3)
        with recording_activated():
            d.today()
        self.assertTrue(is_recorded(self.recorder, date, 'today'))

    def test_datetime_today_test(self):
        d = datetime(1, 2, 3)
        with recording_activated():
            d.today()
        self.assertTrue(is_recorded(self.recorder, datetime, 'today'))

    def test_time_fromisoformat_test(self):
        t = time(1, 2, 3)
        with recording_activated():
            t.fromisoformat('14:05:15')
        self.assertTrue(is_recorded(self.recorder, time, 'fromisoformat'))

    def test_timedelta_total_seconds_test(self):
        td = timedelta(1, 2, 3)
        with recording_activated():
            td.total_seconds()
        self.assertTrue(is_recorded(self.recorder, timedelta, 'total_seconds'))
