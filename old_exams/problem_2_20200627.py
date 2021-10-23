def is_valid_position(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c)
    }

size = int(input())

matrix = []

for _ in range(size):
    row = [x for x in input()]
    matrix.append(row)

burrows = []
for r_i in range(size):
    for c_i in range(size):
        if matrix[r_i][c_i] == "S":
            snake_row, snake_column = r_i, c_i
        elif matrix[r_i][c_i] == "B":
            burrows.append([r_i, c_i])


total_food = 0
game_won = False

while True:
    move = input()
    next_row, next_column = directions[move](snake_row, snake_column)
    matrix[snake_row][snake_column] = "."
    if not is_valid_position(next_row, next_column, matrix):
        break
    if matrix[next_row][next_column] == "B":
        current_burrow_index = burrows.index([next_row, next_column])
        other_burrow_index = (1 - current_burrow_index)
        matrix[next_row][next_column] = "."

        matrix[burrows[other_burrow_index][0]][burrows[other_burrow_index][1]] = "S"
        snake_row = burrows[other_burrow_index][0]
        snake_column = burrows[other_burrow_index][1]

    elif matrix[next_row][next_column] == "*":
        total_food += 1
        matrix[next_row][next_column] = "S"

        snake_row, snake_column = next_row, next_column

    else:
        matrix[next_row][next_column] = "S"

        snake_row, snake_column = next_row, next_column

    if total_food >= 10:
        game_won = True
        break


if game_won:
    print("You won! You fed the snake.")

else:
    print("Game over!")

print(f"Food eaten: {total_food}")
for row in matrix:
    print("".join(row))

