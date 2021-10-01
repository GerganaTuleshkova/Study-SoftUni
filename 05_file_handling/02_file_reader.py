file = open("numbers.txt", "r")

sum = sum([int(x) for x in file.readlines()])

print(sum)