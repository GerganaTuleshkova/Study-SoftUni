rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sum_of_el = 0

for row_index in range(rows):
    row = [int(x) for x in input().split(", ")]
    sum_of_el += sum(row)
    matrix.append(row)

print(sum_of_el)
print(matrix)
