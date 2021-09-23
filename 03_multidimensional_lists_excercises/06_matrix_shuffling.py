def make_matrix():
    rows, columns = [int(x) for x in input().split()]

    matrix = []

    for row_index in range(rows):
        row = [(x) for x in input().split()]
        matrix.append(row)

    return matrix


def is_valid_position(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


matrix = make_matrix()

while True:
    command = input()
    if command == "END":
        break

    command_info = command.split()
    if len(command_info) != 5 or command_info[0] != "swap":
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(n) for n in command_info[1:]]

    if not is_valid_position(row1, col1, matrix) and not is_valid_position(row2, col2, matrix):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        [print(i, end=" ") for i in row]
        print()

