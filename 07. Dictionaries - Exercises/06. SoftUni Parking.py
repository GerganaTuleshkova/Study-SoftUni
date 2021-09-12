n = int(input())
parking_lot = {}

for i in range(n):
    info = input().split()
    action, name = info[0], info[1]
    if action == "register":
        plate = info[2]
        if name not in parking_lot:
            parking_lot[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking_lot[name]}")
    elif action == "unregister":
        if name not in parking_lot:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_lot[name]

for user, plate_num in parking_lot.items():
    print(f"{user} => {plate_num}")
