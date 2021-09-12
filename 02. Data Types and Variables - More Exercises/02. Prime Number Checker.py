number = int(input())

prime = True

for devider in range(2, number):
    if number % devider == 0:
        prime = False
print(prime)