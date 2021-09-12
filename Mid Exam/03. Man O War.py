pirate_ship_status_list = [int(n) for n in input().split(">")]
war_ship_status_list = [int(n) for n in input().split(">")]
max_health_capacity = int(input())
command = input()

ship_won = False

while not command == "Retire":
    info = command.split()
    action = info[0]
    if action == "Fire":
        index = int(info[1])
        damage = int(info[2])
        if 0 <= index < len(war_ship_status_list):
            war_ship_status_list[index] -= damage
            if war_ship_status_list[index] <= 0:
                print("You won! The enemy ship has sunken.")
                ship_won = True
                break

    elif action == "Defend":
        start_index, end_index, damage = int(info[1]), int(info[2]), int(info[3])
        if 0 <= start_index < len(pirate_ship_status_list) and 0 <= end_index < len(pirate_ship_status_list):
            for i in range(start_index, end_index + 1):
                pirate_ship_status_list[i] -= damage
                if pirate_ship_status_list[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    ship_won = True
                    break

    elif action == "Repair":
        index, health = int(info[1]), int(info[2])
        if 0 <= index < len(pirate_ship_status_list):
            pirate_ship_status_list[index] += health
            if pirate_ship_status_list[index] > max_health_capacity:
                pirate_ship_status_list[index] = max_health_capacity

    elif action == "Status":
        sections_that_need_repair = [section for section in pirate_ship_status_list if section < (max_health_capacity * 0.2)]
        print(f"{len(sections_that_need_repair)} sections need repair.")

    command = input()

if not ship_won:
    print(f"Pirate ship status: {sum(pirate_ship_status_list)}")
    print(f"Warship status: {sum(war_ship_status_list)}")
