phones_list = input().split(", ")

command = input()

while not command == "End":
    info = command.split(" - ")
    action = info[0]
    if action == "Add":
        phone = info[1]
        if phone not in phones_list:
            phones_list.append(phone)
    elif action == "Remove":
        phone = info[1]
        if phone in phones_list:
            phones_list.remove(phone)
    elif action == "Bonus phone":
        phone_info = info[1].split(":")
        old_phone, new_phone = phone_info[0], phone_info[1]
        if old_phone in phones_list:
            index_to_insert = phones_list.index(old_phone) + 1
            phones_list.insert(index_to_insert, new_phone)
    elif action == "Last":
        phone = info[1]
        if phone in phones_list:
            phones_list.remove(phone)
            phones_list.append(phone)

    command = input()

print(", ".join(phones_list))