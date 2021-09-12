num_of_cars = int(input())

cars_dict = {}

for n in range(num_of_cars):
    car_info = input().split("|")
    car_brand, mileage, start_fuel = car_info[0], int(car_info[1]), int(car_info[2])
    cars_dict[car_brand] = {"mileage": mileage, "fuel": start_fuel}

command = input()

while not command == "Stop":
    info = command.split(" : ")
    action, car = info[0], info[1]
    if action == "Drive":
        distance = int(info[2])
        fuel = int(info[3])
        if cars_dict[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]["fuel"] -= fuel
            cars_dict[car]["mileage"] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                del cars_dict[car]
    elif action == "Refuel":
        fuel_refill = int(info[2])
        if cars_dict[car]["fuel"] + fuel_refill > 75:
            fuel_refill = 75 - cars_dict[car]["fuel"]
        cars_dict[car]["fuel"] += fuel_refill
        print(f"{car} refueled with {fuel_refill} liters")

    elif action == "Revert":
        kilometers = int(info[2])
        if cars_dict[car]["mileage"] - kilometers < 10000:
            kilometers = cars_dict[car]["mileage"] - 10000
            cars_dict[car]["mileage"] -= kilometers
        else:
            cars_dict[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

ordered_cars = sorted(cars_dict.items(), key=lambda tkvp: (-tkvp[1]["mileage"], tkvp[0]))
for car_name, car_details_dict in ordered_cars:
    print(f"{car_name} -> Mileage: {car_details_dict['mileage']} kms, Fuel in the tank: {car_details_dict['fuel']} lt.")