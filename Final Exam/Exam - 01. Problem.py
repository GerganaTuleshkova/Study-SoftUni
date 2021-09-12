username = input()

command = input()

while not command == "Sign up":
    info = command.split()
    action = info[0]
    if action == "Case":
        direction = info[1]
        if direction == "lower":
            username = username.lower()
        elif direction == "upper":
            username = username.upper()
        print(username)
    elif action == "Reverse":
        start_index = int(info[1])
        end_index = int(info[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index+1]
            substring = substring[::-1]
            print(substring)
    elif action == "Cut":
        substring_to_cut = info[1]
        if substring_to_cut not in username:
            print(f"The word {username} doesn't contain {substring_to_cut}.")
        else:
            #add while if there more then one occurances
            username = username.replace(substring_to_cut, "")
            print(username)
    elif action == "Replace":
        character = info[1]
        username = username.replace(character, "*")
        print(username)
    elif action == "Check":
        character_to_have = info[1]
        if character_to_have in username:
            print("Valid")
        else:
            print(f"Your username must contain {character_to_have}.")


    command = input()