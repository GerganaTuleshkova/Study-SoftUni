def is_valid_index(collection, index):
    if 0 <= index < len(collection):
        return True

friends_list = input().split(", ")

command = input()

while not command == "Report":
    info = command.split()
    action = info[0]
    if action == "Blacklist":
        name = info[1]
        if name not in friends_list:
            print(f"{name} was not found.")
        else:
            friends_list[friends_list.index(name)] = "Blacklisted"
            print(f"{name} was blacklisted.")
    elif action == "Error":
        index = int(info[1])
        if is_valid_index(friends_list, index) and friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
            print(f"{friends_list[index]} was lost due to an error.")
            friends_list[index] = "Lost"
    elif action == "Change":
        index = int(info[1])
        new_name = info[2]
        if is_valid_index(friends_list, index):
            print(f"{friends_list[index]} changed his username to {new_name}.")
            friends_list[index] = new_name

    command = input()
blacklisted_names = [n for n in friends_list if n == "Blacklisted"]
lost_names = [n for n in friends_list if n == "Lost"]
print(f"Blacklisted names: {len(blacklisted_names)}")
print(f"Lost names: {len(lost_names)}")
print(" ".join(friends_list))
