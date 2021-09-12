targeted_cities = {}

command = input()

while not command == "Sail":
    info = command.split("||")
    city, population, gold = info[0], int(info[1]), int(info[2])
    if city not in targeted_cities:
        targeted_cities[city] = [population, gold]
    else:
        targeted_cities[city][0] += population
        targeted_cities[city][1] += gold

    command = input()

command_events = input()

while not command_events == "End":
    events_info = command_events.split("=>")
    action, town = events_info[0], events_info[1]
    if action == "Plunder":
        people, gold_taken = int(events_info[2]), int(events_info[3])
        if town in targeted_cities:
            targeted_cities[town][0] -= people
            targeted_cities[town][1] -= gold_taken
            print(f"{town} plundered! {gold_taken} gold stolen, {people} citizens killed.")
            if targeted_cities[town][0] == 0 or targeted_cities[town][1] == 0:
                print(f"{town} has been wiped off the map!")
                del targeted_cities[town]
    elif action == "Prosper":
        gold_given = int(events_info[2])
        if gold_given < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town][1] += gold_given
            print(f"{gold_given} gold added to the city treasury. {town} now has {targeted_cities[town][1]} gold.")

    command_events = input()

ordered_left_cities = sorted(targeted_cities.items(), key=lambda x: (-(x[1][1]), x[0]))

if len(ordered_left_cities) > 0:
    print(f"Ahoy, Captain! There are {len(ordered_left_cities)} wealthy settlements to go to:")
    for k, v in ordered_left_cities:
        print(f"{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")