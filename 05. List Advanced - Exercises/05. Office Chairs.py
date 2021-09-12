rooms_number = int(input())
free_chairs = 0
room_with_less_chairs = False

for n in range(1, rooms_number + 1):
    information = input().split()
    chairs = len(information[0])
    people = int(information[1])
    if chairs < people:
        print(f"{people - chairs} more chairs needed in room {n}")
        room_with_less_chairs = True
    else:
        free_chairs += chairs - people
if not room_with_less_chairs:
    print(f"Game On, {free_chairs} free chairs left")

