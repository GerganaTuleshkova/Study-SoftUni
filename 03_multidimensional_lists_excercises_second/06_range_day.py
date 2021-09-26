def is_valid_position(row_index, column_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix[0])


def find_shooter_position(matrix):
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "A":
                return r_i, c_i

def count_targets(matrix):
    total_targets = 0
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "x":
                total_targets += 1
    return total_targets


size = 5

matrix = []

for _ in range(size):
    row = input().split()
    matrix.append(row)

directions = {
        "right": lambda r, c, s: (r, c + s),
        "left": lambda r, c, s: (r, c - s),
        "up": lambda r, c, s: (r - s, c),
        "down": lambda r, c, s: (r + s, c)
    }
total_targets = count_targets(matrix)
shooter_r, shooter_c = find_shooter_position(matrix)

number_of_commands = int(input())
targets_shot_count = 0
targets_shots = []

next_r, next_c = shooter_r, shooter_c

for _ in range(number_of_commands):
    next_r, next_c = shooter_r, shooter_c
    command_args = input().split()
    action = command_args[0]
    direction = command_args[1]
    if action == "move":
        steps = int(command_args[2])
        next_r, next_c = directions[direction](next_r, next_c, steps)

        if is_valid_position(next_r, next_c, matrix) and matrix[next_r][next_c] == ".":
            shooter_r, shooter_c = next_r, next_c

    elif action == "shoot":
        steps = 1
        while True:
            next_r, next_c = directions[direction](next_r, next_c, steps)
            if not is_valid_position(next_r, next_c, matrix):
                break
            if matrix[next_r][next_c] == ".":
                continue
            if matrix[next_r][next_c] == "x":
                targets_shot_count += 1
                targets_shots.append([next_r, next_c])
                matrix[next_r][next_c] = "."
                break
    remaining_targets = total_targets - targets_shot_count
    if remaining_targets == 0:
        print(f"Training completed! All {targets_shot_count} targets hit.")
        break

if remaining_targets > 0:
    print(f"Training not completed! {remaining_targets} targets left.")

for el in targets_shots:
    print(el)