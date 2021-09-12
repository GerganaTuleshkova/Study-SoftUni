def is_valid_index(sequence, index):
    if 0 <= index < len(sequence):
        return True

targets = [int(n) for n in input().split()]

command = input()

while not command == "End":
    info = command.split()
    action, index, value = info[0], int(info[1]), int(info[2])
    if action == "Shoot":
        if is_valid_index(targets, index):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        if is_valid_index(targets, index):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if is_valid_index(targets, index-value) and is_valid_index(targets, index + value):
            for i in range(index-value, index + value +1):
                targets.pop(index-value)
        else:
            print("Strike missed!")

    command = input()

print("|".join([str(n) for n in targets]))