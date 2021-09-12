numbers = [int(num) for num in input().split(", ")]
max_num = 0

temp_list = []

while True:
    max_num += 10

    temp_list = [num for num in numbers if num <= max_num]

    print(f"Group of {max_num}'s: {temp_list}")

    numbers = [num for num in numbers if num > max_num]

    temp_list.clear()

    if not numbers:
        break