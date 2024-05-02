import sys
import unittest

from src.step_counting import setup_recording as sr
from src.step_counting.setup_recording import setup_recording, RecodingActivated

from ..utils import is_recorded

import turtle


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

    def test_turtle_forward(self):
        with RecodingActivated():
            turtle.forward(100)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'forward'))

    def test_turtle_backward(self):
        with RecodingActivated():
            turtle.backward(100)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'backward'))

    def test_turtle_right(self):
        with RecodingActivated():
            turtle.right(90)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'right'))

    def test_turtle_left(self):
        with RecodingActivated():
            turtle.left(90)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'left'))

    def test_turtle_setheading(self):
        with RecodingActivated():
            turtle.setheading(180)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'setheading'))

    def test_turtle_speed(self):
        with RecodingActivated():
            turtle.speed(1)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'speed'))

    def test_turtle_delay(self):
        with RecodingActivated():
            turtle.delay(1)
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'delay'))

    def test_turtle_penup(self):
        with RecodingActivated():
            turtle.penup()
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'penup'))

    def test_turtle_pendown(self):
        with RecodingActivated():
            turtle.pendown()
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'pendown'))

    @unittest.skip('Skip testing done as its stops the event loop')
    def test_turtle_done(self):
        with RecodingActivated():
            turtle.done()
        self.assertTrue(is_recorded(self.recorder, turtle, None, 'done'))
