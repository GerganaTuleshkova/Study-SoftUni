def sum_of_negatives(numbers):
    negative_numbers = [n for n in numbers if n < 0]
    return sum(negative_numbers)


def sum_of_positives(numbers):
    positive_numbers = [n for n in numbers if n > 0]
    return sum(positive_numbers)


numbers = [int(n) for n in input().split()]

negative_sum = sum_of_negatives(numbers)
positive_sum = sum_of_positives(numbers)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")