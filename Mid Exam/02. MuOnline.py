health = 100
bitcoins = 0
rooms_count = 0
rooms = input().split("|")
you_died = False

for room in rooms:
    room_info = room.split()
    command = room_info[0]
    number = int(room_info[1])
    rooms_count += 1

    if command == "potion":
        healing_value = number
        if number > 100 - health:
            healing_value = 100 - health
            health = 100
        else:
            health += healing_value

        print(f"You healed for {healing_value} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")

            print(f"Best room: {rooms_count}")
            you_died = True
            break
# if rooms_count == len(rooms):
if not you_died:
    # print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
