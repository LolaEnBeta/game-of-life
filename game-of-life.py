board_size = 5

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

def create_board(board_size):
    board = []
    for row in range(board_size):
        row = []
        for column in range(board_size):
            row.append('-')
        board.append(row)
    return board

def print_board(board):
    for row in board:
        for column in row:
            print(column, " ", end="")
        print("")

board = create_board(board_size)
print_board(board)
       