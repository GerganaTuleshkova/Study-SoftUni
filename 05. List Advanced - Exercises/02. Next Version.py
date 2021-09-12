current_version = [int(num) for num in input().split(".")]

next_version = current_version.copy()

if next_version[2] == 9:
    next_version[2] = 0
    if next_version[1] == 9:
        next_version[0] += 1
        next_version[1] = 0
    else:
        next_version[1] += 1
else:
    next_version[2] += 1

print(".".join([str(x) for x in next_version]))
