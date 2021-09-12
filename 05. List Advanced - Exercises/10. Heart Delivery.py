
    if jump_size + position < len(houses_needs):
        position += +jump_size

    elif jump_size + position >= len(houses_needs):
        position = 0
    if houses_needs[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses_needs[position] -= 2
        if houses_needs[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")
if sum(houses_needs) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([x for x in houses_needs if x !=0])} places.")
