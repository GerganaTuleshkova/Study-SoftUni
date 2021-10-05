from itertools import permutations

chars = input()

for per in permutations(chars):
    print("".join(per))