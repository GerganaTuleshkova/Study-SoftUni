number_of_lines = int(input())
key_word = input()

all_strings_list = []
strings_with_key_list = []

for _ in range(number_of_lines):
    given_string = input()
    all_strings_list.append(given_string)
    if key_word in given_string:
        strings_with_key_list.append(given_string)

print(all_strings_list)
print(strings_with_key_list)
