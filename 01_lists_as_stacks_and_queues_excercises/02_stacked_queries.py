num_of_commands = int(input())

stack = []

for _ in range(num_of_commands):
    command = input()
    if command.startswith("1"):
        pushed_number = int(command.split()[1])
        stack.append(pushed_number)
    elif command == "2":
        if stack:
            stack.pop()
    elif command == "3":
        if stack:
            print(max(stack))
    elif command == "4":
        if stack:
            print(min(stack))

stack_as_string = []
while stack:
    stack_as_string.append(str(stack.pop()))
print(", ".join(stack_as_string))



