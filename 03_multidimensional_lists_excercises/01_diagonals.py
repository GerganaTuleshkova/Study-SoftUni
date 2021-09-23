def make_matrix():
    rows = int(input())

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = make_matrix()
n = len(matrix)

primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(n) for n in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(n) for n in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
