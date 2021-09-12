array = [int(n) for n in input().split()]

command = input()

while not command == "end":
    info = command.split()
    action = info[0]
    if action == "swap":
        index_1 = int(info[1])
        index_2 = int(info[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]
    elif action == "multiply":
        index_1 = int(info[1])
        index_2 = int(info[2])
        array[index_1] *= array[index_2]
    elif action == "decrease":
        for i in range(len(array)):
            array[i] -= 1

    command = input()

print(", ".join([str(n) for n in array]))
