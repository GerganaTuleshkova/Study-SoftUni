def is_valid(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


def get_corresponding_numbers(row, column, matrix):
    return int(matrix[row][0]) + int(matrix[row][-1]) + int(matrix[0][column]) + int(matrix[-1][column])


def get_hit_score(row, column, matrix):
    result = 0

    if not is_valid(row, column, matrix):
        result = 0
        return result

    hit_cell = matrix[row][column]
    if hit_cell.isdigit():
        result = int(hit_cell)
    elif hit_cell == "D":
        result = get_corresponding_numbers(row, column, matrix) * 2
    elif hit_cell == "T":
        result = get_corresponding_numbers(row, column, matrix) * 3
    # else:
    #     result = int(hit_cell)
    return result


def bullseye_hit(row, column, matrix):
    if is_valid(row, column, matrix):
        return matrix[row][column] == "B"
    return False


player1, player2 = input().split(", ")
initial_points = 501


turns = {
    player1: 0,
    player2: 0
}

points = {
    player1: initial_points,
    player2: initial_points
}

size = 7
matrix = []

for _ in range(size):
    row = input().split()
    matrix.append(row)


winner = ""
current_player, other_player = player1, player2
while True:
    hit_row, hit_column = [int(x) for x in input()[1:-1].split(", ")]
    turns[current_player] += 1
    if bullseye_hit(hit_row, hit_column, matrix):
        winner = current_player
        break

    current_score = get_hit_score(hit_row, hit_column, matrix)
    points[current_player] -= current_score

    if points[current_player] <= 0:
        winner = current_player
        break

    current_player, other_player = other_player, current_player

print(f"{winner} won the game with {turns[winner]} throws!")

