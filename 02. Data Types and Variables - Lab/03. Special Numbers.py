number = int(input())

for num in range(1, number + 1):
    special = False
    sum_of_digits = 0
    for digit in str(num):
        sum_of_digits += int(digit)
    if sum_of_digits in [5, 7, 11]:
        special = True
    print(f"{num} -> {special}")
