def check_index_first(index):
    if index == 0:
        return True


def check_index_last(collection, index):
    if index == len(collection)-1:
        return True

def check_row_first(row):
    if row == 0:
        return True

def check_row_last(collection, row):
    if row == len(collection)-1:
        return True

def check_left_is_dot(collection, row, index):
    if check_index_first(collection):
        return False
    if collection[row][index-1] == ".":
        return True


def check_right_is_dot(collection, row, index):
    if check_index_last(collection, index):
        return False
    if collection[row][index+1] == ".":
        return True

def check_up_is_dot(collection, row, index):
    if check_row_first(row):
        return False
    if collection[row-1][index] == ".":
        return True


def check_down_is_dot(collection, row, index):
    if check_row_last(collection, row):
        return False
    if collection[row + 1][index] == ".":
        return True


n = int(input())
board = []

for line in range(n):
    line_as_list = input().split()
    board.append(line_as_list)
row_length = len(board[0])

max_connected_dots = 1
connected_dots = []

for r in range(n):

    for i in range(len(board[0])):
        if board[r][i] == ".":
            if (not check_row_first(r) and board[r-1][i] == ".") \
                    or (not check_row_last(board, r) and board[r+1][i] == ".") \
                    or (not check_index_first(i) and board[r][i-1] == ".") \
                    or (not check_index_last(board,i) and board[r][i+1]):
                connected_dots.append([r, i])

            # if len(set(connected_dots)) >= max_connected_dots:
            #     max_connected_dots = len(set(connected_dots))
line = [connected_dots[0]]

current_dot = connected_dots[0]
if check_right_is_dot(connected_dots,current_dot[0], current_dot[1]):
    line.append()


print(connected_dots)
