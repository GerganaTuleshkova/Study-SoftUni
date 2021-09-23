def make_matrix():
    rows = int(input())

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


matrix = make_matrix()

even_matrix = [[n for n in row if n % 2 == 0] for row in matrix]

print(even_matrix)