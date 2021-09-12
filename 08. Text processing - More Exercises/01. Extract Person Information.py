num_of_lines = int(input())
name = ""
age = ""

for line in range(num_of_lines):
    info = input()
    for i in range(len(info)):
        if info[i] == "@":
            next_ch = info[i + 1]
            while not next_ch == "|":

                name += next_ch
                i += 1
                next_ch = info[i + 1]
        if info[i] == "#":
            next_ch = (info[i+1])
            while not next_ch == "*":
                age += next_ch
                i += 1
                next_ch = (info[i + 1])
    print(f"{name} is {age} years old.")
    name = ""
    age = ""