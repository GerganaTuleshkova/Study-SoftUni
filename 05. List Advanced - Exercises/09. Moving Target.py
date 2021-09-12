targets = [int(x) for x in input().split()]

command = input()
while not command == "End":
    instruction = command.split()
    action = instruction[0]
    index = int(instruction[1])
    value = int(instruction[2])
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= (index - value) and (index + value) < len(targets):
            for i in range(index - value, index + value + 1):
                targets.pop(index - value)
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(x) for x in targets]))
