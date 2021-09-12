#numbers = input().split(", ")
numbers = list(map(lambda x: int(x), input().split(", ")))
# even_nums_indices = []
#
# for n in range(len(numbers)):
#     #if int(numbers[n]) % 2 == 0:
#     if numbers[n] % 2 == 0:
#         even_nums_indices.append(n)
#
# print(even_nums_indices)

print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])