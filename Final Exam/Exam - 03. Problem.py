entire_input = input()

my_dict = {}

words_info_list = entire_input.split(" | ")
for word_info_string in words_info_list:
    word_info = word_info_string.split(": ")
    word = word_info[0]
    definition = word_info[1]
    if word not in my_dict:
        my_dict[word] = [definition]
    else:
        my_dict[word].append(definition)

tested_words = input().split(" | ")

command = input()


ordered_by_length = {}
for k, v in my_dict.items():
    #sorted_definitions = sorted(v, key=len)
    v.sort(key=len, reverse=True)
    ordered_by_length[k] = v



if command == "Test":
    for tested_word in tested_words:
        if tested_word in ordered_by_length:
            print(f"{tested_word}:")
            for definition in ordered_by_length[tested_word]:
                print(f" -{definition}")

elif command == "Hand Over":
    for key, value in sorted(ordered_by_length.items()):
        print(key, end=" ")