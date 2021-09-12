raw_key = input()


command = input()

while not command == "Generate":
    info_list = command.split(">>>")
    action = info_list[0]
    if action == "Contains":
        substring = info_list[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        direction = info_list[1]
        start_index = int(info_list[2])
        end_index = int(info_list[3])

        substring = raw_key[start_index:end_index]
        if direction == "Upper":
            substring = substring.upper()
        elif direction == "Lower":
            substring = substring.lower()
        result_key = raw_key[:start_index] + substring + raw_key[end_index:]
        raw_key = result_key
        print(raw_key)
    elif action == "Slice":
        start_index = int(info_list[1])
        end_index = int(info_list[2])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)

    command = input()

print(f"Your activation key is: {raw_key}")