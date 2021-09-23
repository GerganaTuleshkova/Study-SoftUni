def is_valid_row_index(index, matrix):
    if 0 <= index < len(matrix):
        return True
    return False


def is_valid_column_index(index, matrix):
    if 0 <= index < len(matrix[0]):
        return True
    return False


game_lost = False
game_won = False

r_n, c_n = [int(n) for n in input().split()]
matrix = []

for i in range(r_n):
    row = [x for x in input()]
    matrix.append(row)

    if "P" in row:
        player_r = i
        player_c = row.index("P")

moves = input()

for move in moves:
    next_move_r = player_r
    next_move_c = player_c

    if move == "U":
        next_move_r -= 1
    elif move == "D":
        next_move_r += 1
    elif move == "L":
        next_move_c -= 1
    elif move == "R":
        next_move_c += 1


    matrix[player_r][player_c] = "."
    bunnies_list = []

    for bunny_row in range(r_n):
        for bunny_column in range(c_n):
            if matrix[bunny_row][bunny_column] == "B":
                bunnies_list.append((bunny_row, bunny_column))

    for bunny_indecis in bunnies_list:
        bunny_row = bunny_indecis[0]
        bunny_column = bunny_indecis[1]
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if is_valid_row_index(bunny_row + i, matrix) \
                        and is_valid_column_index(bunny_column + j, matrix) \
                        and matrix[bunny_row + i][bunny_column + j] == "." and abs(i + j) == 1:
                        matrix[bunny_row + i][bunny_column + j] = "B"
                elif is_valid_row_index(bunny_row + i, matrix) \
                    and is_valid_column_index(bunny_column + j, matrix) \
                    and matrix[bunny_row + i][bunny_column + j] == "P":
                    game_lost = True
                    break
    if not is_valid_row_index(next_move_r, matrix) or not is_valid_column_index(next_move_c, matrix):
        game_won = True

        break
    if matrix[next_move_r][next_move_c] == "B":
        game_lost = True
        player_r = next_move_r
        player_c = next_move_c
        break


    player_r = next_move_r
    player_c = next_move_c


for row in matrix:
    [print(i, end="") for i in row]
    print()


if game_won:
    print(f"won: {player_r} {player_c}")

if game_lost:
    print(f"dead: {player_r} {player_c}")


