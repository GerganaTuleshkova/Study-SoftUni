given_string = input()
list_capitals = []

for index in range(len(given_string)):

    if 65 <= ord(given_string[index]) <= 90:
        list_capitals.append(index)
    else:
        continue

print(list_capitals)
