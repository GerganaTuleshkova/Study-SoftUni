def is_valid_position(row_index, column_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix[0])


def find_alice_position(matrix):
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "A":
                return r_i, c_i


n = int(input())

matrix = []

for _ in range(n):
    row = input().split()
    matrix.append(row)

directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c)
    }

total_tea = 0
alice_r, alice_c = find_alice_position(matrix)
next_r, next_c = alice_r, alice_c
matrix[alice_r][alice_c] = "*"

move = input()
while not move == "":
    next_r, next_c = directions[move](next_r, next_c)
    if not is_valid_position(next_r, next_c, matrix):
        print("Alice didn't make it to the tea party.")
        break

    if matrix[next_r][next_c] == "R":
        print("Alice didn't make it to the tea party.")
        matrix[next_r][next_c] = "*"
        break

    if matrix[next_r][next_c].isdigit():
        total_tea += int(matrix[next_r][next_c])

    matrix[next_r][next_c] = "*"

    if total_tea >= 10:
        print("She did it! She went to the party.")
        matrix[next_r][next_c] = "*"
        break

    move = input()

for row in matrix:
    print(" ".join(row))
