def characters_between(char_1, char_2):
    result = ""
    for n in range(ord(char_1)+1, ord(char_2)):
        result += chr(n) + " "
    return result


first_char = input()
second_char = input()
print(characters_between(first_char, second_char))