divisor = int(input())
limit = int(input())

number = limit
number_not_found = True
while number_not_found:
    if number % divisor == 0:
        number_not_found = False
        break
    else:
        number -= 1
print(number)