def read_players_info():
    player_1_name = input("Player one name: ")
    player_2_name = input("Player two name: ")
    player_1_sign, player_2_sign = get_players_signs(player_1_name)
    player_1 = [player_1_name, player_1_sign]
    player_2 = [player_2_name, player_2_sign]
    return player_1, player_2


def get_players_signs(player_1):
    while True:
        player_1_sign = input(f"{player_1}, would you like to play with 'X' or '0'? ")
        player_1_sign = player_1_sign.upper()
        if player_1_sign in "X0":
            player_2_sign = "X" if player_1_sign == "0" else "0"
            return player_1_sign, player_2_sign
        print(f"{player_1}, this is not a valid sign. Please choose between 'X' and '0'. Let's try again :)")


def print_board(board):
    for row in board:
        print(f"| {' | '.join([str(x) if x != '' else ' ' for x in row ])} |")


def print_start_board(board):
    i = 1
    for row_index in range(len(board)):
        for column_index in range (len(board[0])):
            board[row_index][column_index] = i
            i += 1
    print("This is the numeration of the board:")
    print_board(board)
    for row_index in range(len(board)):
        for column_index in range (len(board[0])):
            board[row_index][column_index] = ""


def is_empty(selected_position, board):
    r, c = get_coords_by_position(selected_position)
    return board[r][c] == ""


def get_coords_by_position(position):
    position_mapper = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
    }

    return position_mapper[position]


def choose_position(board, current_player):
    """Returns the row and the column of the selected position if valid"""

    while True:
        selected_position = 0
        try:
            selected_position = int(input(f"{current_player[0]}, choose a free position [1-9]: "))
        except ValueError:
            print("This is not a valid position.")
            continue
        if selected_position not in range(1, 10):
            print("This is not a valid position number.")
            continue
        if not is_empty(selected_position, board):
            print("This position is not free.")
            continue
        row, column = get_coords_by_position(selected_position)
        return row, column


def apply_position(board, row, column, current_player):
    board[row][column] = current_player[1]


def is_board_full(board):
    for row in board:
        is_row_full = all([el != "" for el in row])
        if not is_row_full:
            return False
    return True


def check_if_wins(board, current_player):
    sign = current_player[1]
    size = len(board)

    # check horizontal
    for row in board:
        if all([el == sign for el in row]):
            return True

    # check vertical
    for col_index in range(size):
        won = True
        for row_index in range(size):
            if board[row_index][col_index] != sign:
                won = False
                break
        if won:
            return True

    # check primary diagonal
    won = True
    for index in range(size):
        if board[index][index] != sign:
            won = False
            break
    if won:
        return True

    # check secondary diagonal
    won = True
    for index in range(size):
        if board[index][size - 1 - index] != sign:
            won = False
            break
    return won


def play(board):
    # get the players names and signs
    player_1, player_2 = read_players_info()

    # set current player to player 1
    current_payer, other_player = player_1, player_2

    # print the board with numbers
    print_start_board(board)

    # print who starts first
    print(f"{current_payer[0]} starts first!")

    # start playing
    while True:

        row, col = choose_position(board, current_payer)
        apply_position(board, row, col, current_payer)
        print_board(board)

        if check_if_wins(board, current_payer):
            print(f"{current_payer[0]} won!")
            break
        if is_board_full(board):
            print("Draw!")
            break

        current_payer, other_player = other_player, current_payer


board = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
play(board)

