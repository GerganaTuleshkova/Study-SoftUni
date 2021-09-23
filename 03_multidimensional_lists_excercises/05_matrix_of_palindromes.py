r, c = [int(n) for n in input().split()]

matrix = []

start = ord("a")
middle = ord("a")


for r_index in range(r):
    matrix.append([])
    for c_index in range(c):
        current_element = chr(start) + chr(middle + r_index + c_index) + chr(start)
        matrix[r_index].append(current_element)
    start += 1

for row_index in range(len(matrix)):
    [print(n, end=" ") for n in matrix[row_index]]
    print()
