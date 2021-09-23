def make_matrix():
    rows, columns = [int(x) for x in input().split(", ")]

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = make_matrix()

highest_sum = 0
r = 0
c = 0

n = len(matrix)
m = len(matrix[0])

for row_index in range(n-2, -1, -1):
    for column_index in range(m - 2, -1, -1):
        sum_submatrix = matrix[row_index][column_index] + \
                        matrix[row_index][column_index + 1] + \
                        matrix[row_index + 1][column_index] + \
                        matrix[row_index + 1][column_index + 1]
        if sum_submatrix >= highest_sum:
            highest_sum = sum_submatrix
            r, c = row_index, column_index

print(matrix[r][c], matrix[r][c+1])
print(matrix[r + 1][c], matrix[r + 1][c+1])
print(highest_sum)