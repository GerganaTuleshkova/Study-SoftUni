word_to_hide = input().split(", ")

given_text = input()

for word in word_to_hide:
    while word in given_text:
        given_text = given_text.replace(word, ("*"*len(word)))

print(given_text)