import unittest

def calculate_neighbours(board, current_box_row, current_box_column):
    neighbours = 0
    # Calculate neighbours here!
    for row_index in range(current_box_row - 1, current_box_row + 2):
        for column_index in range(current_box_column - 1, current_box_column + 2):
            if row_index == current_box_row and column_index == current_box_column:
                continue
            
            if board[row_index][column_index] == '0':
                neighbours += 1
    return neighbours

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