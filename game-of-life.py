board_size = 5
def create_board(board_size):
    board = []
    for row in range(board_size):
        row = []
        for column in range(board_size):
            column = "-"
            row.append(column)
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(row)

board = create_board(board_size)
print_board(board)
       