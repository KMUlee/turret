from GameLogic import Minesweeper
import unittest

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.g = Minesweeper()

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
        self.assertEqual(self.g.find(tile,5,5),answer)

if __name__ == '__main__':
    unittest.main()