def make_matrix():
    rows, columns = [int(x) for x in input().split(" ")]
    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split(" ")]
        matrix.append(row)

    return matrix


matrix = make_matrix()


highest_sum = 0
r = 0
c = 0

n = len(matrix)
m = len(matrix[0])

for row_index in range(n-2):
    for column_index in range(m - 2):
        sum_submatrix = matrix[row_index][column_index] + \
                        matrix[row_index][column_index + 1] + \
                        matrix[row_index][column_index + 2] +\
                        matrix[row_index + 1][column_index] + \
                        matrix[row_index + 1][column_index + 1] +\
                        matrix[row_index + 1][column_index + 2] + \
                        matrix[row_index + 2][column_index] + \
                        matrix[row_index + 2][column_index + 1] + \
                        matrix[row_index + 2][column_index + 2]
        if sum_submatrix >= highest_sum:
            highest_sum = sum_submatrix
            r, c = row_index, column_index

print(f"Sum = {highest_sum}")
# print(matrix[r][c], matrix[r][c + 1], matrix[r][c + 2])
# print(matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r+1][c + 2])
# print(matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r+2][c + 2])

for i in range(r, r + 3):
    for j in range(c, c + 3):
        print(matrix[i][j], end=" ")
    print()

