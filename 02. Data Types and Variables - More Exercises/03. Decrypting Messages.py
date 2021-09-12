key = int(input())
lines = int(input())

for line in range(1, lines + 1):
    letter = input()
    print(f"{chr(ord(letter)+ key)}",end="")