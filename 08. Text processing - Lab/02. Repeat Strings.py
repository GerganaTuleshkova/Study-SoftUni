given_strings = input().split()

for word in given_strings:
    print(f"{word*len(word)}", end="")