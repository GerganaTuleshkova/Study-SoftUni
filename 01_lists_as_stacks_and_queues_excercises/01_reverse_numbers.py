given_numbers = [int(num) for num in input().split()]
reversed_numbers = []
for n in given_numbers:
    reversed_numbers.append(n)

while reversed_numbers:
    print(reversed_numbers.pop(), end=" ")
