num_of_wagons = int(input())
train = [0]*num_of_wagons

command = input()
while not command == "End":
    instructions = command.split(" ")
    action = instructions[0]
    if action == "add":
        people_to_add = int(instructions[1])
        train[-1] += people_to_add
    elif action == "insert":
        index = int(instructions[1])
        people = int(instructions[2])
        train[index] += people
    elif action == "leave":
        index = int(instructions[1])
        people = int(instructions[2])
        train[index] -= people
    command = input()

print(train)

