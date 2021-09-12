first_list = input().split(", ")
second_list = input().split(", ")
found_strings = []

for word in first_list:
    for searched_word in second_list:
        if word in searched_word:
            found_strings.append(word)
            break

print(found_strings)