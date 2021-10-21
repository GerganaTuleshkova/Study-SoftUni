def numbers_searching(*args):
    given_numbers = list(args)
    min_number = min(given_numbers)
    max_number = max(given_numbers)

    duplicates = []
    result = []
    for number in range(min_number, max_number + 1):
        if number not in given_numbers:
            result.append(number)
        elif given_numbers.count(number) > 1:
            duplicates.append(number)
    result.append(duplicates)
    return result



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
