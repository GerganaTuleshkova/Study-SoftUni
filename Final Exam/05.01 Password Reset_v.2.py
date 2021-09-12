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
        index = int(info[1])
        length = int(info[2])
        password = password[:index] + password[index+length:]
        print(password)
    elif action == "Substitute":
        substring = info[1]
        new_string = info[2]
        if substring in password:
            while substring in password:
                password = password.replace(substring, new_string)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")