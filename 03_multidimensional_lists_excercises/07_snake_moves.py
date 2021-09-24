rows, columns = [int(x) for x in input().split()]
matrix = []

for row_index in range(rows):
    row = [""] * columns
    matrix.append(row)

snake = input()

count = 0
for r_index in range(rows):
    if r_index % 2 == 0:
        for c_index in range(columns):
            matrix[r_index][c_index] = snake[(count % len(snake))]
            count += 1
    else:
        for c_index in range(columns - 1, -1, -1):
            matrix[r_index][c_index] = snake[(count % len(snake))]
            count += 1

for row in matrix:
    [print(i, end="") for i in row]
    print()
