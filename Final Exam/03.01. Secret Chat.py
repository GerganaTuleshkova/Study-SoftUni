hidden_message = input()

command = input()

while not command == "Reveal":
    info = command.split(":|:")
    action = info[0]
    if action == "InsertSpace":
        index = int(info[1])
        hidden_message = hidden_message[:index] + " " + hidden_message[index:]
        print(hidden_message)
    elif action == "Reverse":
        substring = info[1]
        if substring in hidden_message:
            found_at_index = hidden_message.find(substring)
            hidden_message = hidden_message[:found_at_index] \
                             + hidden_message[found_at_index + len(substring):] + substring[::-1]
            print(hidden_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring_to_change = info[1]
        replacement = info[2]
        while substring_to_change in hidden_message:
            found_at_index_2 = hidden_message.find(substring_to_change)
            hidden_message = hidden_message[:found_at_index_2] + replacement \
                             + hidden_message[found_at_index_2 + len(substring_to_change):]
        print(hidden_message)
    command = input()

print(f"You have a new text message: {hidden_message}")