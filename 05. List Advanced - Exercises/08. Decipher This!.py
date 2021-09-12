given_words = input().split()
deciphered_text = []

for word in given_words:
    word_as_list = [i for i in word]
    nums = [ch for ch in word_as_list if ch.isnumeric()]

    ascii_num = int("".join(nums))
    for i in range(len(nums)):
        word_as_list.pop(0)
    word_as_list.insert(0, chr(ascii_num))
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
    deciphered_text.append("".join(letter for letter in word_as_list))

print(" ".join(deciphered_text))


