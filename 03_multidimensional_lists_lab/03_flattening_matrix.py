def make_matrix():
    rows = int(input())

    matrix = []

    for row_index in range(rows):
        row = [int(x) for x in input().split(", ")]
        matrix.append(row)

    return matrix


flattened_matrix = [n for sublist in make_matrix() for n in sublist]

print(flattened_matrix)

