def make_matrix():
    rows, columns = [int(x) for x in input().split(", ")]

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix


matrix = make_matrix()

sum_columns = [0 for n in range(len(matrix[0]))]

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[0])):
        sum_columns[column_index] += matrix[row_index][column_index]


[print(n) for n in sum_columns]
