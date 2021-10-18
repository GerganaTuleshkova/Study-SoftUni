def best_list_pureness(numbers: list, rotations):
    pureness = sum([index * numbers[index] for index in range(len(numbers))])
    best_pureness_round = 0
    for rotation in range(1, rotations + 1):
        numbers.insert(0, numbers.pop())
        current_pureness = sum([index * numbers[index] for index in range(len(numbers))])
        if pureness < current_pureness:
            pureness = current_pureness
            best_pureness_round = rotation

    return f"Best pureness {pureness} after {best_pureness_round} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
