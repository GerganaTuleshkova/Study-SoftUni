given_string = input()
given_string = given_string.lower()

key_word_count = given_string.count("sand") \
                 + given_string.count("water") \
                 + given_string.count("fish") \
                 + given_string.count("sun")

print(key_word_count)
