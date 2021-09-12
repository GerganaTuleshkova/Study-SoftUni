word_1, word_2 = input().split()

sum = 0

remaining_len = len(word_1) - len(word_2)
is_word_1_shorter = False
longer_word = word_1
shorter_word_len = len(word_2)


if len(word_1) < len(word_2):
    shorter_word_len = len(word_1)
    remaining_len = len(word_2) - len(word_1)
    is_word_1_shorter = True
    longer_word = word_2

for i in range(0, shorter_word_len):
    sum += ord(word_1[i]) * ord(word_2[i])


for i in range(shorter_word_len, shorter_word_len+remaining_len):
    sum += ord(longer_word[i])

print(sum)