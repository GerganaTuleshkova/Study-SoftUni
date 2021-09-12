number_of_lines = int(input())
sum_of_char = 0
for num in range(1, number_of_lines +1):
    letter = input()
    sum_of_char += ord(letter)

print(f"The sum equals: {sum_of_char}")