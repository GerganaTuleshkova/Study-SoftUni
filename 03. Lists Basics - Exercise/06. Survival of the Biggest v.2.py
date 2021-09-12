num_list = input().split()
n = int(input())

numbers_list = [int(x) for x in num_list]

for _ in range(n):
    numbers_list.remove(min(numbers_list))

numbers_list = [str(x) for x in numbers_list]

print(", ".join(numbers_list))