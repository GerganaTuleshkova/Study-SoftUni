def is_knight(board, row, col):
    board_size = len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def count_affected_knight(r_index, c_index, matrix):
    affected_knights = 0
    for r in [-2, -1, 1, 2]:
        for c in [-2, -1, 1, 2]:
            if abs(r) + abs(c) == 3 and is_knight(matrix, r_index + r, c_index + c):
                affected_knights += 1
    return affected_knights


n = int(input())

board = []

for _ in range(n):
    row = [ch for ch in input()]
    board.append(row)

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for r_i in range(len(board)):
        for c_i in range(len(board)):
            if board[r_i][c_i] == "0":
                continue
            count = count_affected_knight(r_i, c_i, board)
            if count > max_count:
                max_count, knight_row, knight_col = count, r_i, c_i
    if max_count == 0:
        break

    board[knight_row][knight_col] = "0"
    removed_knights += 1


print(removed_knights)
