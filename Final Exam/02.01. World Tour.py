given_text = input()

command = input()

while not command == "Travel":
    info = command.split(":")
    action = info[0]
    if action == "Add Stop":
        index = int(info[1])
        string_to_insert = info[2]
        if 0 <= index < len(given_text):
            given_text = given_text[:index] + string_to_insert + given_text[index:]
        print(given_text)
    elif action == "Remove Stop":
        start_index = int(info[1])
        end_index = int(info[2])
        if 0 <= start_index < len(given_text) and 0 <= end_index < len(given_text):
            given_text = given_text[:start_index] + given_text[end_index+1:]
        print(given_text)
    elif action == "Switch":
        old_string = info[1]
        new_string = info[2]
        if old_string in given_text:
            #while old_string in given_text:
            given_text = given_text.replace(old_string, new_string)
        print(given_text)

    command = input()

print(f"Ready for world tour! Planned stops: {given_text}")