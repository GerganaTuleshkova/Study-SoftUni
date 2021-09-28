def find_sum_be_criteria(numbers, criteria):
    count = len(numbers)
    if criteria == "Odd":
        sum_by_criteria = sum([n for n in numbers if n % 2 != 0])
    elif criteria == "Even":
        sum_by_criteria = sum([n for n in numbers if n % 2 == 0])
    return sum_by_criteria * count


criteria = input()
numbers = [int(n) for n in input().split()]

print(find_sum_be_criteria(numbers, criteria))