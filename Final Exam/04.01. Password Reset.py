password = input()

command = input()

while not command == "Done":
    info = command.split()
    action = info[0]
    if action == "TakeOdd":
        new_pass = ""
        for i in range(1, len(password), 2):
            new_pass += password[i]
        password = new_pass
        print(password)
    elif action == "Cut":
        index_to_start, length = int(info[1]), int(info[2])
        password = password[:index_to_start] + password[(index_to_start+length):]
        print(password)

    elif action == "Substitute":
        substring, substitute = info[1], info[2]
        if substring not in password:
            print("Nothing to replace!")
        else:

            while substring in password:
                index_to_start_replace = password.find(substring)
                password = password[:index_to_start_replace] + substitute \
                           + password[(index_to_start_replace + len(substring)):]
            print(password)

    command = input()

print(f"Your password is: {password}")