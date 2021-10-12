from fibonacci import create_fib_sequence,find_n_in_fib

while True:
    command = input()
    if command == "Stop":
        break

    command_args = command.split()
    action = command_args[0]
    number = int(command_args[-1])
    if action == "Create":
        sequence = create_fib_sequence(number)
        print(" ".join([str(n) for n in sequence]))
    elif action == "Locate":
        print(find_n_in_fib(sequence, number))
