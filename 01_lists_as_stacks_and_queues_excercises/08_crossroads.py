from collections import deque


class Car:
    def __init__(self, model):
        self.model = model
        self.length = len(model)


green_light_duration = int(input())
free_window = int(input())

cars_in_line = deque()

passed_cars_count = 0


while True:
    command = input()
    has_passed = True
    if command == "END":
        print("Everyone is safe.")
        print(f"{passed_cars_count} total cars passed the crossroads.")
        break

    elif command == "green":
        green_time_left = green_light_duration
        window_time_left = free_window

        while cars_in_line:
            entering_car = cars_in_line.popleft()
            green_time_left -= entering_car.length
            if green_time_left < 0:
                window_time_left += green_time_left
                if window_time_left < 0:
                    has_passed = False
                    hit_at = entering_car.model[window_time_left]
                    print("A crash happened!")
                    print(f"{entering_car.model} was hit at {hit_at}.")
                    break
                else:
                    passed_cars_count += 1
                    break

            else:
                passed_cars_count += 1
                if green_time_left == 0:
                    break

        if not has_passed:
            break

    else:
        cars_in_line.append(Car(command))




