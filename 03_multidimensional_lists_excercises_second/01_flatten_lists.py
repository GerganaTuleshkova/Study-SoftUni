lists_stack = input().split("|")
matrix = []

for _ in range(len(lists_stack)):
    current_list = lists_stack.pop().split()
    matrix.append(current_list)


([print(n, end=" ") for row in matrix for n in row])