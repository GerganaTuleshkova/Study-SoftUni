loot_list = input().split("|")

command = input()

while not command == "Yohoho!":
    info = command.split()
    action = info[0]
    if action == "Loot":
        for index in range(1, len(info)):
            if info[index] not in loot_list:
                loot_list.insert(0, info[index])
    elif action == "Drop":
        index = int(info[1])
        if 0 <= index < len(loot_list):
            item = loot_list.pop(index)
            loot_list.append(item)
    elif action == "Steal":
        count_to_remove = int(info[1])
        if count_to_remove > len(loot_list):
            count_to_remove = len(loot_list)

        removed_items = loot_list[-count_to_remove:]
        del loot_list[-count_to_remove:]
        print(", ".join(removed_items))

    command = input()

sum_of_lengths = 0
for item in loot_list:
    sum_of_lengths += len(item)
if loot_list:
    print(f"Average treasure gain: {sum_of_lengths/len(loot_list):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
