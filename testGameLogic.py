from GameLogic import Turret
import unittest

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.g = Turret()

    def tearDown(self):
        pass

    def testLogic(self):
