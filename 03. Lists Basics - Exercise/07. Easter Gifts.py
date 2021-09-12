given_string = input()
gifts_list = given_string.split(" ")

while True:
    command = input()

    if command == "No Money":
        break
    command_list = command.split(" ")
    if command_list[0] == "OutOfStock":
        item_to_remove = command_list[1]
        for i in range(len(gifts_list)):
            if gifts_list[i] == item_to_remove:
                gifts_list[i] = "None"
    if command_list[0] == "Required":
        if 0< int(command_list[2]) < len(gifts_list):
            gifts_list[int(command_list[2])] = command_list[1]
    if command_list[0] == "JustInCase":
        gifts_list[-1] = command_list[1]

for item in gifts_list:
    if not item == "None":
        print(item,end=" ")
