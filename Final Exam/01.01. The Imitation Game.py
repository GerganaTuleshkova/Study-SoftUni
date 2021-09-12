message = input()

command = input()

while not command == "Decode":
    info = command.split("|")
    action = info[0]
    if action == "Move":
        num_of_letter = int(info[1])
        # part_1 = message[num_of_letter:]
        # part_2 = message[:num_of_letter]
        message = message[num_of_letter:] + message[:num_of_letter]
    elif action == "Insert":
        index = int(info[1])
        substring = info[2]
        message = message[:index] + substring + message[index:]
    elif action == "ChangeAll":
        substring_to_change = info[1]
        replacement = info[2]
        message = message.replace(substring_to_change, replacement)

    command = input()

print(f"The decrypted message is: {message}")