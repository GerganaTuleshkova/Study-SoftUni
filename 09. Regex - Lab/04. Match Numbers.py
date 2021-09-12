import re

text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

numbers = re.finditer(pattern, text)

for number in numbers:
    print(number.group(), end=" ")

# second way to print the results
# nums = [n.group() for n in numbers]
# print(*nums)