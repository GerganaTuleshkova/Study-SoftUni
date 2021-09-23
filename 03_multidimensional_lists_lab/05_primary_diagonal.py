def make_matrix():
    rows = int(input())

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)

    return matrix


matrix = make_matrix()

sum_primary_diagonal = 0

n = len(matrix)
m = len(matrix[0])

for row_index in range(n):
    for column_index in range(m):
        if row_index == column_index:
            sum_primary_diagonal += matrix[row_index][column_index]

print(sum_primary_diagonal)