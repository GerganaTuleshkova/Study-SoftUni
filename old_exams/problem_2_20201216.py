def is_valid_position(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


string = input()

# create the matrix
n = int(input())
matrix = []

for i in range(n):
    row = list(input())
    matrix.append(row)

# find the position of the player
for r_i in range(n):
    for c_i in range(n):
        if matrix[r_i][c_i] == "P":
            player_row = r_i
            player_col = c_i

# get the number of moves
number_of_moves = int(input())

moves = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "down": lambda r, c: (r + 1, c),
    "up": lambda r, c: (r - 1, c),
}

for i in range(number_of_moves):
    next_move = input()
    next_move_r, next_move_c = moves[next_move](player_row, player_col)

    if not is_valid_position(next_move_r, next_move_c, matrix):
        if string:
            string = string[:-1]
        continue

    matrix[player_row][player_col] = "-"
    player_row, player_col = next_move_r, next_move_c
    thing_on_move = matrix[next_move_r][next_move_c]
    if thing_on_move.isalpha():
        string += thing_on_move
        matrix[next_move_r][next_move_c] = "P"

print(string)
for row_index in range(n):
    for col_index in range(n):
        print(matrix[row_index][col_index], end="")
    print()






