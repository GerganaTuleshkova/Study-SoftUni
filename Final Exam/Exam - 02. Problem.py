import re

num_of_passwords = int(input())

pattern = r"^(?P<sur>.+)>(?P<numbers>[0-9]{3})\|(?P<l_letters>[a-z]{3})\|(?P<u_letters>[A-Z]{3})\|(?P<symbols>[^<>]{3})<(?P=sur)$"

for n in range(num_of_passwords):
    password_to_check = input()
    password_checked = re.fullmatch(pattern, password_to_check)

    if not password_checked:
        print("Try another password!")
    else:
        encrypted_password = password_checked.group("numbers") + password_checked.group("l_letters") \
                             + password_checked.group("u_letters") + password_checked.group("symbols")
        print(f"Password: {encrypted_password}")
