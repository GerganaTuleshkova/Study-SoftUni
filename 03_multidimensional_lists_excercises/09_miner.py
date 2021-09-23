def is_valid_row_index(index, matrix):
    if 0 <= index < len(matrix):
        return True
    return False


def is_valid_column_index(index, matrix):
    if 0 <= index < len(matrix[0]):
        return True
    return False


n = int(input())

moves = [x for x in input().split()]
matrix = []
total_coal = 0
collected_coal = 0

for i in range(n):
    row = [x for x in input().split()]
    matrix.append(row)
    total_coal += row.count("c")
    if "s" in row:
        start_r = i
        start_c = row.index("s")

game_finished = True

for move in moves:
    if move == "up" and is_valid_row_index(start_r - 1, matrix):
        start_r -= 1
    elif move == "down" and is_valid_row_index(start_r + 1, matrix):
        start_r += 1
    elif move == "right" and is_valid_column_index(start_c + 1, matrix):
        start_c += 1
    elif move == "left" and is_valid_column_index(start_c - 1, matrix):
        start_c -= 1
    if matrix[start_r][start_c] == "e":
        print(f"Game over! ({start_r}, {start_c})")
        game_finished = False
        break
    elif matrix[start_r][start_c] == "c":
        collected_coal += 1
        matrix[start_r][start_c] = "*"
        if collected_coal == total_coal:
            print(f"You collected all coal! ({start_r}, {start_c})")
            game_finished = False
            break


if game_finished:
    print(f"{total_coal - collected_coal} pieces of coal left. ({start_r}, {start_c})")