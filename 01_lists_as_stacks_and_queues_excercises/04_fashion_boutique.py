clothes_stack = [int(el) for el in input().split()]

rack_capacity = int(input())
number_of_racks = 0

while clothes_stack:
    current_load = 0
    while current_load < rack_capacity:
        if clothes_stack:
            next_cloth = clothes_stack[-1]
            if next_cloth <= rack_capacity - current_load:
                current_load += clothes_stack.pop()
                if current_load == rack_capacity:
                    number_of_racks += 1
                    break
            else:
                number_of_racks += 1
                break

        else:
            number_of_racks += 1
            break

print(number_of_racks)