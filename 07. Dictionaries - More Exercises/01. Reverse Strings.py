given_word = input()

while not given_word == "end":
    reversed_word = given_word[::-1]
    print(f"{given_word} = {reversed_word}")
    given_word = input()