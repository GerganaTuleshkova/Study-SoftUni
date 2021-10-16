from math import floor


def is_valid_index(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


moves = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "down": lambda r, c: (r + 1, c),
    "up": lambda r, c: (r - 1, c),
}

size = int(input())

matrix = []

for _ in range(size):
    row = input().split()
    matrix.append(row)

for r_i in range(size):
    for c_i in range(size):
        if matrix[r_i][c_i] == "P":
            player_row, player_column = r_i, c_i

next_row, next_column = player_row, player_column
path = []
total_coins = 0
game_lost = False

while True:
    command = input()
    if command == "":
        break
    if command not in moves.keys():
        continue

    matrix[player_row][player_column] = 0
    next_row, next_column = moves[command](next_row, next_column)

    if not is_valid_index(next_row, next_column, matrix) or matrix[next_row][next_column] == "X":
        game_lost = True
        total_coins = floor(total_coins * 0.50)
        break
    coins_to_collect = int(matrix[next_row][next_column])
    path.append([next_row, next_column])
    total_coins += coins_to_collect
    matrix[next_row][next_column] = 0

    if total_coins >= 100:
        break


if not game_lost and total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")

print("Your path:")
for step in path:
    print(step)