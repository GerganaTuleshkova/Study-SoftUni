def make_matrix():
    rows, columns = [int(x) for x in input().split(" ")]
    matrix = []

    for row_index in range(rows):
        row = [x for x in input().split(" ")]
        matrix.append(row)

    return matrix


matrix = make_matrix()
square_matrices_count = 0

n = len(matrix)
m = len(matrix[0])

for row_index in range(n-1):
    for column_index in range(m-1):
        if \
                matrix[row_index][column_index] == matrix[row_index][column_index + 1] and \
                matrix[row_index][column_index] == matrix[row_index + 1][column_index] and \
                matrix[row_index][column_index] == matrix[row_index + 1][column_index + 1]:
            square_matrices_count += 1

print(square_matrices_count)