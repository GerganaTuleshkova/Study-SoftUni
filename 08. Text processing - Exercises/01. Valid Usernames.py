usernames_to_check = input().split(", ")

for username in usernames_to_check:
    if 3 <= len(username) <= 16:
        is_valid = True
        for letter in username:
            if not (letter.isdigit() or letter.isalpha() or letter == "-" or letter == "_"):
                is_valid = False
            if letter == " ":
                is_valid = False
        if is_valid:
            print(username)
