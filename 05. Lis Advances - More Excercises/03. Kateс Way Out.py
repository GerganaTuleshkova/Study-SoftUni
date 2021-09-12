def no_move_possible_check(collection, row_n, index):
    row = collection[row_n - 1]
    if not row_is_first_or_last(collection, row_n):
        previous_row = collection[row_n - 2]
        next_row = collection[row_n]
        if row[index - 1] == "#" and row[index + 1] == "#" and previous_row[index] == "#" and next_row[index] == "#":
            return True

def row_is_first_or_last(collection, row_n):

    if row_n == 1 or row_n == len(collection):
        return True

def position_in_start_or_end(collection, row_n, index):
    if index == 0 or index == len(collection[row_n]) - 1:
        return True

def look_for_empty_space(collection, row_n, index):
    row = collection[row_n-1]
    moves_out = 0
    new_row_n = row_n
    new_index = index
    if row_is_first_or_last(collection, row_n):
        moves_out += 1
        return moves_out, row_n, index, collection

    previous_row = collection[row_n-2]
    next_row = collection[row_n]
    if row[index - 1] == " ":
        new_index = index - 1
    elif row[index + 1] == " ":
        new_index = index - 1
    elif previous_row[index] == " ":
        new_row_n = row_n - 1
    elif next_row[index] == " ":
        new_row_n = row_n + 1
    collection[row_n - 1][index] = "#"
    moves_out += 1
    return moves_out, new_row_n, new_index, collection



rows = int(input())
maze = []

for row in range(1, rows+1):
    blocks = input()
    row_as_list = [block for block in blocks]
    maze.append(row_as_list)
    if "k" in blocks:
        kate_position_in_row = blocks.index("k")
        kate_in_row = row

kate_is_not_out = True
total_moves = 0
new_row_n = kate_in_row
new_index = kate_position_in_row
collection = maze

while kate_is_not_out:
    if no_move_possible_check(maze, kate_in_row, kate_position_in_row):
        print("Kate cannot get out")
        break
    else:
        moves_out, new_row_n, new_index, collection = look_for_empty_space(maze, kate_in_row, kate_position_in_row)

        if row_is_first_or_last(collection, new_row_n) \
                or position_in_start_or_end(collection, new_row_n, new_index):
            moves_out += 1
            kate_is_not_out = False
        kate_in_row = new_row_n
        maze = collection
        kate_position_in_row = new_index
        total_moves += moves_out
if not kate_is_not_out:
    print(f"Kate got out in {total_moves} moves")


