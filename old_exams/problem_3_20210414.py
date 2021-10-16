def flights(*args):
    flights_info = {}
    details = args
    for i in range(0, len(details), 2):
        destination = details[i]
        if destination == "Finish":
            break
        passengers = int(details[i+1])
        if destination not in flights_info:
            flights_info[destination] = 0
        flights_info[destination] += passengers
    return flights_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
