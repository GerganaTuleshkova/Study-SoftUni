def is_valid_position(row_index, column_index, matrix):
    return 0 <= row_index < len(matrix) and 0 <= column_index < len(matrix[0])


n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

command = input()

while not command == "END":
    command_args = command.split()
    action = command_args[0]
    row, column, value = [int(x) for x in command_args[1:]]
    if not is_valid_position(row, column, matrix):
        print("Invalid coordinates")

    elif action == "Add":
        matrix[row][column] += value
    elif action == "Subtract" :
        matrix[row][column] -= value

    command = input()

for row in matrix:
    print(" ".join([str(n) for n in row]))

