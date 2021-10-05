from itertools import combinations
names = input().split(", ")
count = int(input())

for combination in combinations(names, count):
    print(", ".join(combination))