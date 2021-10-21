def is_valid_position(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[1])

def count_near_bombs(row, column, matrix):
    count_of_near_bombs = 0

    # check North
    if is_valid_position(row - 1, column, matrix) and matrix[row - 1][column] == "*":
        count_of_near_bombs += 1
    # check South
    if is_valid_position(row + 1, column, matrix) and matrix[row + 1][column] == "*":
        count_of_near_bombs += 1
    # check East
    if is_valid_position(row, column + 1, matrix) and matrix[row][column + 1] == "*":
        count_of_near_bombs += 1
    # check West
    if is_valid_position(row, column - 1, matrix) and matrix[row][column - 1] == "*":
        count_of_near_bombs += 1
    # check NE
    if is_valid_position(row - 1, column + 1, matrix) and matrix[row - 1][column + 1] == "*":
        count_of_near_bombs += 1
    # check NW
    if is_valid_position(row - 1, column - 1, matrix) and matrix[row - 1][column - 1] == "*":
        count_of_near_bombs += 1
    # check SE
    if is_valid_position(row + 1, column + 1, matrix) and matrix[row + 1][column + 1] == "*":
        count_of_near_bombs += 1
    # check SW
    if is_valid_position(row + 1, column - 1, matrix) and matrix[row + 1][column - 1] == "*":
        count_of_near_bombs += 1

    return count_of_near_bombs



size = int(input())
bombs_count = int(input())

field = []

for _ in range(size):
    field.append([""*size for _ in range(size)])

for _ in range(bombs_count):
    bomb_row, bomb_column = input()[1:-1].split(", ")
    bomb_row = int(bomb_row)
    bomb_column = int(bomb_column)
    field[bomb_row][bomb_column] = "*"

for r_i in range(size):
    for c_i in range(size):
        if field[r_i][c_i] == "*":
            continue
        field[r_i][c_i] = count_near_bombs(r_i, c_i, field)

for row in field:
    print(" ".join([str(x) for x in row]))
