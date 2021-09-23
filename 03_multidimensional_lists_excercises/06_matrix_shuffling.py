def make_matrix():
    rows, columns = [int(x) for x in input().split()]

    matrix = []

    for row_index in range(rows):
        row = [(x) for x in input().split()]
        matrix.append(row)

    return matrix


matrix = make_matrix()

while True:
    command = input()
    if command == "END":
        break

    command_info = command.split()
    if len(command_info) != 5 or command_info[0] != "swap":
        print("Invalid input!")
        continue
    else:
        row1, col1, row2, col2 = [int(n) for n in command_info[1:]]
        if \
                (row1 > len(matrix) - 1) \
                or (row2 > len(matrix) - 1) \
                or (col1 > len(matrix[0]) - 1) \
                or (col2 > len(matrix[0]) - 1)\
                or (0 > row1) \
                or (0 > row2) \
                or (0 > col1) \
                or (0 > col2):
            print("Invalid input!")
            continue

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        for row in matrix:
            [print(i, end=" ") for i in row]
            print()

