from collections import deque

num_of_pumps = int(input())

# make 2 queues: one for the fuel from each pump and second for the distance to next pump
fuel_queue = deque()
km_queue = deque()

# add the elements to the respective queue
for i in range(num_of_pumps):
    fuel, km_to_next_pump = input().split()
    fuel = int(fuel)
    km_to_next_pump = int(km_to_next_pump)
    fuel_queue.append(fuel)
    km_queue.append(km_to_next_pump)

# create list where all indices of the pumps as a possible start will be stored
possible_start_indexes = []

# try with each pump as a start -> number of tries = number of pumps
for i in range(len(fuel_queue)):
    fuel_in_tank = 0
    # create copy of the queues so that for next attempt we have the original queues
    km_queue_copy = km_queue.copy()
    fuel_queue_copy = fuel_queue.copy()

    is_possible = True
    # change the queues to start with next element
    for _ in range(i):
        move_fuel = fuel_queue_copy.popleft()
        fuel_queue_copy.append(move_fuel)

        move_km = km_queue_copy.popleft()
        km_queue_copy.append(move_km)

    # check if fuel including the refills is enough to go through each distance
    while km_queue_copy:
        fuel_in_tank += fuel_queue_copy.popleft()
        if fuel_in_tank >= km_queue_copy[0]:
            spent_fuel = km_queue_copy.popleft()
            fuel_in_tank -= spent_fuel
        else:
            is_possible = False
            break
    if is_possible:
        possible_start_indexes.append(i)

print(possible_start_indexes[0])
