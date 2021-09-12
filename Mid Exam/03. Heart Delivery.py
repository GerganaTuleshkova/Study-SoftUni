houses_needs = [int(n) for n in input().split("@")]

command = input()
current_index = 0

while not command == "Love!":
    info = command.split()
    jump_length = int(info[1])
    current_index += jump_length
    if current_index > len(houses_needs) - 1:
        current_index = 0
    if houses_needs[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses_needs[current_index] -= 2
        if houses_needs[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")
if sum(houses_needs) == 0:
    print("Mission was successful.")
else:
    failed_houses = [house for house in houses_needs if house > 0]
    print(f"Cupid has failed {len(failed_houses)} places.")