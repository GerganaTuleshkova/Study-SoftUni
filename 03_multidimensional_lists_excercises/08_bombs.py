def is_valid_row_index(index, matrix):
    if 0 <= index < len(matrix):
        return True
    return False


def is_valid_column_index(index, matrix):
    if 0 <= index < len(matrix[0]):
        return True
    return False


rows = int(input())

matrix = []

for row_index in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

indeces_info = input().split()

for bomb_info in indeces_info:
    bomb_r, bomb_c = [int(n) for n in bomb_info.split(",")]
    if matrix[bomb_r][bomb_c] <= 0:
        continue
    bomb_power = matrix[bomb_r][bomb_c]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if \
                    is_valid_row_index(bomb_r + i, matrix) \
                    and is_valid_column_index(bomb_c + j, matrix) \
                    and matrix[bomb_r + i][bomb_c + j] > 0:
                matrix[bomb_r + i][bomb_c + j] -= bomb_power

alive_cells = []

for r in matrix:
    alive_cells += [x for x in r if x > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")

for row in matrix:
    [print(i, end=" ") for i in row]
    print()