import re

numbers_found = []

while True:
    text = input()

    if not text:
        break
    pattern = r"\d+"
    numbers = re.findall(pattern, text)
    for num in numbers:
        numbers_found.append(num)



print(" ".join(numbers_found))

