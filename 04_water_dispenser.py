from collections import deque

water_qty = int(input())

queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()
    if command == "End":
        break
    elif command.startswith("refill"):
        refill_qty = int(command.split()[1])
        water_qty += refill_qty
    else:
        wanted_qty = int(command)
        if wanted_qty <= water_qty:
            print(f"{queue.popleft()} got water")
            water_qty -= wanted_qty
        else:
            print(f"{queue.popleft()} must wait")
print(f"{water_qty} liters left")
