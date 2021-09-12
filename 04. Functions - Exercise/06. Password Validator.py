def password_validator(password):
    is_valid = True
    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    for character in password:
        if ord(character) < 48 or 58 <= ord(character) <= 64 or 91 <= ord(character) <= 96 or ord(character) >= 123:
            is_valid = False
            print("Password must consist only of letters and digits")
            break
    digits_count = 0
    for character in password:
        if 48 <= ord(character) <= 57:
            digits_count += 1
    if digits_count < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


passowrd_enetered = input()
password_validator(passowrd_enetered)