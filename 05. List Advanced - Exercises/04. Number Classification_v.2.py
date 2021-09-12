numbers_list = [int(n) for n in input().split(", ")]

positive_numbers = [num for num in numbers_list if num >= 0]
negative_numbers = [num for num in numbers_list if num < 0]
even_nums = [num for num in numbers_list if num % 2 == 0]
odd_nums = [num for num in numbers_list if num % 2 != 0]

# positives = ", ".join([str(n) for n in positive_numbers])
# negatives = ", ".join([str(n) for n in negative_numbers])
# evens = ", ".join([str(n) for n in even_nums])
# odds = ", ".join([str(n) for n in odd_nums])
print(f"Positive: "+", ".join([str(n) for n in positive_numbers]))
print(f"Negative: " + ", ".join([str(n) for n in negative_numbers]))
print(f"Even: "+", ".join([str(n) for n in even_nums]))
print(f"Odd: "+", ".join([str(n) for n in odd_nums]))