items_list = input().split(", ")

command = input()

while not command == "Craft!":
    info = command.split(" - ")
    action, item = info[0], info[1]
    if action == "Collect":
        if item not in items_list:
            items_list.append(item)
    elif action == "Drop":
        if item in items_list:
            items_list.remove(item)
    elif action == "Combine Items":
        split_items = item.split(":")
        old_item, new_item = split_items[0], split_items[1]
        if old_item in items_list:
            index_to_append = items_list.index(old_item)+1
            items_list.insert(index_to_append,new_item)
    elif action == "Renew":
        if item in items_list:
            items_list.remove(item)
            items_list.append(item)

    command = input()

print(", ".join(items_list))