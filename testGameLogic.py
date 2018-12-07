from GameLogic import Turret
import unittest

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.g = Turret()

    def tearDown(self):
        pass

    def testLogic(self):
        tile = [['-', '-', '-', '*', '-'],
                ['*', '-', '*', '-', '-'],
                ['-', '-', '-', '-', '*'],
                ['-', '-', '-', '*', '*'],
                ['*', '*', '-', '-', '-'],
                ]
        answer = [['1', '2', '2', '*', '1'],
                ['*', '2', '*', '3', '2'],
                ['1', '2', '2', '4', '*'],
                ['2', '2', '2', '*', '*'],
                ['*', '*', '2', '2', '2']]
        self.g.find(tile,5,5)
        print("fuck")
        self.assertEqual(self.g.find(tile,5,5),answer)
