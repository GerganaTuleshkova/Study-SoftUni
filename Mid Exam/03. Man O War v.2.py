def is_valid_index(collection, index):
    if 0 <= index < len(collection):
        return True


pirate_ship = [int(n) for n in input().split(">")]

warship = [int(n) for n in input().split(">")]

max_health_capacity = int(input())
command = input()

ship_is_sunk = False
while not command == "Retire":
    info = command.split()
    action = info[0]
    if action == "Fire":
        index, damage = int(info[1]), int(info[2])
        if is_valid_index(warship, index):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                ship_is_sunk = True
                break
    elif action == "Defend":
        start_index, end_index, damage = int(info[1]), int(info[2]), int(info[3])
        if is_valid_index(pirate_ship, start_index) and is_valid_index(pirate_ship, end_index):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    ship_is_sunk = True
                    break
    elif action == "Repair":
        index, health = int(info[1]), int(info[2])
        if is_valid_index(pirate_ship, index):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity
    elif action == "Status":
        sections_that_need_repair = [n for n in pirate_ship if n < max_health_capacity*0.20]
        print(f"{len(sections_that_need_repair)} sections need repair.")

    command = input()

if not ship_is_sunk:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")