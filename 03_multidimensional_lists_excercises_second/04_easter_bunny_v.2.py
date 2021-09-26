def is_valid_position(row_index, column_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix[0])


def find_bunny_position(matrix):
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "B":
                return r_i, c_i


def move_left(matrix):
    eggs_collected = 0
    bunny_r, bunny_c = find_bunny_position(matrix)
    possible_next_move = True
    while possible_next_move:
        if 0 <= bunny_c - 1 < len(matrix[0]) and matrix[bunny_r][bunny_c - 1] != "X":
            eggs_collected += int(matrix[bunny_r][bunny_c - 1])
            bunny_c -= 1
            continue
        possible_next_move = False
    return eggs_collected


def move_right(matrix):
    eggs_collected = 0
    bunny_r, bunny_c = find_bunny_position(matrix)
    possible_next_move = True
    while possible_next_move:
        if 0 <= bunny_c + 1 < len(matrix[0]) and matrix[bunny_r][bunny_c + 1] != "X":
            eggs_collected += int(matrix[bunny_r][bunny_c + 1])
            bunny_c += 1
            continue
        possible_next_move = False
    return eggs_collected


def move_up(matrix):
    eggs_collected = 0
    bunny_r, bunny_c = find_bunny_position(matrix)
    possible_next_move = True
    while possible_next_move:
        if 0 <= bunny_r - 1 < len(matrix[0]) and matrix[bunny_r - 1][bunny_c] != "X":
            eggs_collected += int(matrix[bunny_r - 1][bunny_c])
            bunny_r -= 1
            continue
        possible_next_move = False
    return eggs_collected


def move_down(matrix):
    eggs_collected = 0
    bunny_r, bunny_c = find_bunny_position(matrix)
    possible_next_move = True
    while possible_next_move:
        if 0 <= bunny_r + 1 < len(matrix[0]) and matrix[bunny_r + 1][bunny_c] != "X":
            eggs_collected += int(matrix[bunny_r + 1][bunny_c])
            bunny_r += 1
            continue
        possible_next_move = False
    return eggs_collected


def show_step(matrix, direction, r, c):

    directions = {
        "right": [r, c + 1],
        "left": [r, c - 1],
        "up": [r - 1, c],
        "down": [r + 1, c]
    }
    next_position = directions[direction]
    row, col = next_position
    if is_valid_position(row, col, matrix) \
            and matrix[row][col] != "X":

        return next_position[0], next_position[1]
    return r, c


n = int(input())
matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)

bunny_r, bunny_c = find_bunny_position(matrix)
directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c)
    }

max_eggs_collected = float("-inf")
max_direction = ""
max_path_steps = []

for direction, step in directions.items():
    eggs_collected = 0
    current_path = []
    current_r, current_c = bunny_r, bunny_c

    while True:
        current_r, current_c = step(current_r, current_c)
        if not is_valid_position(current_r, current_c, matrix):
            break

        if matrix[current_r][current_c] == "X":
            break

        eggs_collected += int(matrix[current_r][current_c])
        current_path.append([current_r, current_c])

    if eggs_collected > max_eggs_collected:
        max_eggs_collected = eggs_collected
        max_direction = direction
        max_path_steps = current_path

print(max_direction)
[print(s) for s in max_path_steps]
print(max_eggs_collected)