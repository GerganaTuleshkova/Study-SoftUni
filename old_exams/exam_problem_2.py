def is_valid_position(row, column, matrix):
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])


def get_trow_score(row, column, matrix):
    score = 0
    if not is_valid_position(row, column, matrix) or not matrix[row][column] == "B":
        return score

    for r_i in range(size):
        if matrix[r_i][column].isdigit():
            score += int(matrix[r_i][column])
    matrix[row][column] = 0
    return score


size = 6

matrix = []

points = 0

for _ in range(size):
    row = input().split()
    matrix.append(row)

for _ in range(3):
    coordinates = [int(x) for x in input()[1:-1].split(", ")]
    row, column = coordinates
    current_score = get_trow_score(row, column, matrix)
    points += current_score


if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif points < 200:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif points < 300:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")