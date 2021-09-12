words_list = input().split()

even_length_words = [word for word in words_list if len(word) % 2 == 0]

for word in even_length_words:
    print(word)