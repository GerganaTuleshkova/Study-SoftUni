events_list = input().split("|")
energy = 100
coins = 100

for element in events_list:
    pair = element.split("-")
    item = pair[0]
    number = int(pair[1])
    if item == "rest":
        gained_energy = number
        if energy + gained_energy > 100:
            gained_energy = 100 - energy
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif item == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > number:
            coins -= number
            print(f"You bought {item}.")

        else:
            print(f"Closed! Cannot afford {item}.")
            coins -= number
            break

if coins > 0:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")