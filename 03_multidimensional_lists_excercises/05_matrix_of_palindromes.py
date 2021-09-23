r, c = [int(n) for n in input().split()]

start = ord("a")

# 1st option with make of a matrix

#matrix = []
# for r_index in range(r):
#     matrix.append([])
#     for c_index in range(c):
#         current_element = chr(start + r_index) + chr(start + r_index + c_index) + chr(start + r_index)
#         matrix[r_index].append(current_element)
#
# for row_index in range(len(matrix)):
#     [print(n, end=" ") for n in matrix[row_index]]
#     print()

for r_index in range(r):
    for c_index in range(c):
        print(chr(start + r_index) + chr(start + r_index + c_index) + chr(start + r_index), end=" ")

    print()



