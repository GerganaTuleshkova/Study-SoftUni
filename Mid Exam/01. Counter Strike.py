energy = int(input())
wins = 0

command = input()

while not command == "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        exit()
    if wins % 3 == 0:
        energy += wins

    command = input()

print(f"Won battles: {wins}. Energy left: {energy}")