def make_matrix():
    rows = int(input())

    matrix = []

    for row_index in range(rows):
        row = input()
        matrix.append(row)

    return matrix



matrix = make_matrix()
searched_symbol = input()

n = len(matrix)

symbol_found = False
for row_index in range(n):
    if searched_symbol in matrix[row_index]:
        column_index = matrix[row_index].index(searched_symbol)
        symbol_found = True
        break
    else:
        continue

if symbol_found:
    print(f"({row_index}, {column_index})")
else:
    print(f"{searched_symbol} does not occur in the matrix")

