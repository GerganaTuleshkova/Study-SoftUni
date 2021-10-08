def draw_board(rows, columns):
    board = []
    for row in range(rows):
        board.append([None] * columns)
    return board


def print_board(board):
    for row in board:
        print([0 if el is None else el for el in row])


def is_valid_column(column_index, board):
    return 0 <= column_index < len(board[0])


def is_not_full_column(column_index, board):
    return board[0][column_index] is None


def play(board, connect_count):
    current_player, other_player = 1, 2
    while True:
        selected_column = choose_column(current_player, board)
        print(selected_column + 1)
        row, col = apply_selection(current_player, selected_column, board)
        print_board(board)
        if check_if_winning(board, row, col, connect_count):
            print(f"The winner is player {current_player}")
            return

        current_player, other_player = other_player, current_player


def choose_column(player, board):
    while True:
        try:
            selected_column = int(input(f"Player {player} please choose a column\n")) - 1
            if is_valid_column(selected_column, board) and is_not_full_column(selected_column, board):
                return selected_column
            else:
                print("This is not a valid column or the column is full already. Please choose another one.")

        except ValueError:
            print("This is not a valid column. Please choose another one.")


def apply_selection(player, selected_column, board):
    for row_index in range(len(board)-1, -1, -1):
        if board[row_index][selected_column] is None:
            board[row_index][selected_column] = player
            return row_index, selected_column


def get_right_cells(board, row, column, connect_count):
    right_cells_values = []
    right_index_limit = min(column + connect_count, len(board[0]))
    for c_index in range(column, right_index_limit):
        right_cells_values.append(board[row][c_index])
    return right_cells_values


def get_left_cells(board, row, column, connect_count):
    left_cells_values = []
    left_index_limit = max(column - connect_count + 1, 0)
    for c_index in range(left_index_limit, column + 1):
        left_cells_values.append(board[row][c_index])
    return left_cells_values


def get_up_cells(board, row, column, connect_count):
    up_cells_values = []
    up_index_limit = max(row - connect_count + 1, 0)
    for r_index in range(up_index_limit, row + 1):
        up_cells_values.append(board[r_index][column])
    return up_cells_values


def get_down_cells(board, row, column, connect_count):
    down_cells_values = []
    down_index_limit = min(row + connect_count, len(board))
    for r_index in range(row, down_index_limit):
        down_cells_values.append(board[r_index][column])
    return down_cells_values


def get_down_right_diagonal_cells(board, row, column, connect_count):
    down_right_cells_values = []
    down_index_max = min(row + connect_count - 1, len(board) - 1)
    right_index_max = min(column + connect_count - 1, len(board[0]) - 1)
    down_right_diagonal_range = min(down_index_max - row, right_index_max - column)
    for addition in range(down_right_diagonal_range + 1):
        down_right_cells_values.append(board[row + addition][column + addition])
    return down_right_cells_values


def get_down_left_diagonal_cells(board, row, column, connect_count):
    down_left_cells_values = []
    down_index_max = min(row + connect_count - 1, len(board) - 1)
    left_index_min = max(column - connect_count + 1, 0)
    down_left_diagonal_range = min(down_index_max - row, column - left_index_min)
    for addition in range(down_left_diagonal_range + 1):
        down_left_cells_values.append(board[row + addition][column - addition])
    return down_left_cells_values


def get_up_right_diagonal_cells(board, row, column, connect_count):
    up_right_cells_values = []
    up_index_min = max(row - connect_count + 1, 0)
    right_index_max = min(column + connect_count - 1, len(board[0]) - 1)
    up_right_diagonal_range = min(row - up_index_min, right_index_max - column)
    for addition in range(up_right_diagonal_range + 1):
        up_right_cells_values.append(board[row - addition][column + addition])
    return up_right_cells_values


def get_up_left_diagonal_cells(board, row, column, connect_count):
    up_left_cells_values = []
    up_index_min = max(row - connect_count + 1, 0)
    left_index_min = max(column - connect_count + 1, 0)
    up_left_diagonal_range = min(row - up_index_min, column - left_index_min)
    for addition in range(up_left_diagonal_range + 1):
        up_left_cells_values.append(board[row - addition][column - addition])
    return up_left_cells_values


def check_if_winning(board, row, column, connect_count):
    all_directions = [
        get_right_cells(board, row, column, connect_count),
        get_left_cells(board, row, column, connect_count),
        get_up_cells(board, row, column, connect_count),
        get_down_cells(board, row, column, connect_count),
        get_down_right_diagonal_cells(board, row, column, connect_count),
        get_down_left_diagonal_cells(board, row, column, connect_count),
        get_up_right_diagonal_cells(board, row, column, connect_count),
        get_up_left_diagonal_cells(board, row, column, connect_count)
        ]

    for direction in all_directions:
        if len(direction) == connect_count and len(set(direction)) == 1:
            return True
    return False


board = draw_board(6, 7)
# board = [
#     [0, 0, 0, 1, 2, 1, None],
#     [1, 2, 1, 1, 1, 1, None],
#     [1, 2, 1, 1, 2, 1, None],
#     [1, 2, 1, 1, 2, 1, None],
#     [1, 2, 1, 1, 2, 1, None],
#     [1, 2, 1, 1, 2, 1, None],
# ]
# #
# board = [
#     [None, -3, None, None, None, 30, None],
#     [None, None, -1, None, 20, None, None],
#     [2, 3, 4, 1, 6, 7, 8],
#     [None, None, 1, 1, None, None, None],
#     [None, None, None, 2, None, None, None],
#     [None, None, None, 3, None, None, None],
# ]

print_board(board)
play(board, 4)
# print(check_if_winning(board, 0, 4, 4))
#print(choose_column(1,board))
