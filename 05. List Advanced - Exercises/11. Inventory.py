collecting_items = input().split(", ")

command = input()

while not command == "Craft!":
    instruction = command.split(" - ")
    action = instruction[0]
    item = instruction[1]
    if action == "Collect":
        if item in collecting_items:
            continue
        else:
            collecting_items.append(item)
    elif action == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)
    elif action == "Combine Items":
        swapping_items = item.split(":")
        old_item = swapping_items[0]
        new_item = swapping_items[1]
        if old_item in collecting_items:
            collecting_items.insert(collecting_items.index(old_item)+1,new_item)
    elif action == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

    command = input()

print(", ".join(collecting_items))