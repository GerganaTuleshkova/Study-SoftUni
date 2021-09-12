def read_and_execute(input_type, executable):
    if input_type == "int":
        result = f"{int(executable) * 2}"
    elif input_type == "real":
        result = f"{float(executable) * 1.5:.2f}"
    elif input_type == "string":
        result = f"${executable}$"

    return result


input_type = input()
executable = input()

print(read_and_execute(input_type, executable))
