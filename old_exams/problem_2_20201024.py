def get_king_coordinates(board):
    for r_i in range(len(board)):
        for c_i in range(len(board[0])):
            if board[r_i][c_i] == "K":
                return r_i, c_i


def get_capturing_queens_coordinates(board):
    size = len(board)
    king_row, king_column = get_king_coordinates(board)
    capturing_queens = []
    # check North
    for r_i in range(king_row, -1, -1):
        if board[r_i][king_column] == "Q":
            capturing_queens.append([r_i, king_column])
            break

    # check South
    for r_i in range(king_row, size):
        if board[r_i][king_column] == "Q":
            capturing_queens.append([r_i, king_column])
            break

    # check East
    for c_i in range(king_column + 1, size):
        if board[king_row][c_i] == "Q":
            capturing_queens.append([king_row, c_i])
            break

    # check West
    for c_i in range(king_column, -1, -1):
        if board[king_row][c_i] == "Q":
            capturing_queens.append([king_row, c_i])
            break

    # check NE
    min_ne_range = min((size - 1 - king_column), king_row)
    for i in range(min_ne_range + 1):
        if board[king_row - i][king_column + i] == "Q":
            capturing_queens.append([king_row - i, king_column + i])
            break

    # check SE
    min_se_range = min((size - 1 - king_column), (size - 1 - king_row))
    for i in range(min_se_range + 1):
        if board[king_row + i][king_column + i] == "Q":
            capturing_queens.append([king_row + i, king_column + i])
            break

    # check NW
    min_nw_range = min(king_column, king_row)
    for i in range(min_nw_range + 1):
        if board[king_row - i][king_column - i] == "Q":
            capturing_queens.append([king_row - i, king_column - i])
            break

    # check SW
    min_sw_range = min(king_column, (size - 1 - king_row))
    for i in range(min_sw_range + 1):
        if board[king_row + i][king_column - i] == "Q":
            capturing_queens.append([king_row + i, king_column - i])
            break

    return capturing_queens


size = 8
board = []

for _ in range(size):
    row = input().split()
    board.append(row)

queens_that_can_capture = get_capturing_queens_coordinates(board)

if not queens_that_can_capture:
    print("The king is safe!")
else:
    [print(coords) for coords in queens_that_can_capture]