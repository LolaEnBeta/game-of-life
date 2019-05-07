import unittest
from GameOfLife import calculate_neighbours

class GameOfLifeTest(unittest.TestCase):

    def test_neighbours(self):

        board = [
            ["-", "0", "-"],
            ["-", "-", "-"],
            ["-", "0", "0"]
        ]
        neighbours = calculate_neighbours(board, 1, 1)
        self.assertEqual(neighbours, 3)

    def test_neighbours_big_board(self):
    
        board = [
            ["-", "0", "-", "0"],
            ["-", "0", "-", "0"],
            ["-", "0", "-", "0"],
            ["-", "0", "0", "0"]
        ]
        neighbours = calculate_neighbours(board, 1, 2)
        self.assertEqual(neighbours, 6)

unittest.main()