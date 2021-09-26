def is_valid_position(row_index, column_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix[0])


def find_santa_position(matrix):
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "S":
                return r_i, c_i


def count_nice_kids(matrix):
    nice_kids = 0
    for r_i in range(len(matrix)):
        for c_i in range(len(matrix[0])):
            if matrix[r_i][c_i] == "V":
                nice_kids += 1
    return nice_kids


def get_houses_in_range(matrix, santa_r, santa_c):
    houses = []
    if is_valid_position(santa_r, santa_c - 1, matrix):
        houses.append([santa_r, santa_c - 1])
    if is_valid_position(santa_r, santa_c + 1, matrix):
        houses.append([santa_r, santa_c + 1])
    if is_valid_position(santa_r - 1, santa_c, matrix):
        houses.append([santa_r - 1, santa_c])
    if is_valid_position(santa_r + 1, santa_c, matrix):
        houses.append([santa_r + 1, santa_c])
    return houses


all_presents = int(input())
size = int(input())
matrix = []
for _ in range(size):
    row = input().split()
    matrix.append(row)

santa_r, santa_c = find_santa_position(matrix)
nice_kids_count = count_nice_kids(matrix)
all_nice_kids = nice_kids_count

directions = {
        "right": lambda r, c: (r, c + 1),
        "left": lambda r, c: (r, c - 1),
        "up": lambda r, c: (r - 1, c),
        "down": lambda r, c: (r + 1, c)
    }

command = input()

while not command == "Christmas morning":
    presents_finished = False
    next_r, next_c = directions[command](santa_r, santa_c)

    if not is_valid_position(next_r, next_c, matrix):
        break
    if matrix[next_r][next_c] == "V":
        all_presents -= 1
        nice_kids_count -= 1

    if matrix[next_r][next_c] == "X":
        all_presents -= 1

    elif matrix[next_r][next_c] == "C":
        houses_in_range = get_houses_in_range(matrix, next_r, next_c)
        for row, col in houses_in_range:
            if matrix[row][col] == "V":
                all_presents -= 1
                nice_kids_count -= 1
                matrix[row][col] = "-"
                if all_presents == 0:
                    break
            elif matrix[row][col] == "X":
                all_presents -= 1
                matrix[row][col] = "-"
                if all_presents == 0:
                    break
    matrix[santa_r][santa_c] = "-"
    matrix[next_r][next_c] = "S"
    santa_r, santa_c = next_r, next_c

    if all_presents == 0:
        break
    command = input()

if all_presents == 0 and nice_kids_count > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(" ".join(row))

if nice_kids_count == 0:
    print(f"Good job, Santa! {all_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")