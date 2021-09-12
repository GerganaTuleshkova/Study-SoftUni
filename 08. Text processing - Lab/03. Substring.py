string_to_remove = input()
given_string = input()

while string_to_remove in given_string:
    given_string = given_string.replace(string_to_remove, "")

print(given_string)
