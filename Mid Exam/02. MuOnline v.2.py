health = 100
bitcoins = 0

rooms = input().split("|")
is_killed = False

for room in rooms:
    info_room = room.split()
    action, number = info_room[0], int(info_room[1])
    if action == "potion":
        difference = 100 - health

        if difference <= number:
            number = difference
        health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif action == "chest":
        print(f"You found {number} bitcoins.")
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {rooms.index(room)+1}")
            is_killed = True
            break

if not is_killed:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
