strings = input().split()
result = 0

for string in strings:
    number = int(string[1:-1])
    first_letter = string[0]
    last_letter = string[-1]
    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    else:
        number *= (ord(first_letter) - 96)
    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    else:
        number += (ord(last_letter) - 96)
    result += number

print(f"{result:.2f}")