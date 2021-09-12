numbers_list = input().split(", ")

positive_numbers = [int(num) for num in numbers_list if int(num) >= 0]
negative_numbers = [int(num) for num in numbers_list if int(num) < 0]
even_nums = [int(num) for num in numbers_list if int(num) % 2 == 0]
odd_nums = [int(num) for num in numbers_list if int(num) % 2 != 0]

positives = ", ".join([str(n) for n in positive_numbers])
negatives = ", ".join([str(n) for n in negative_numbers])
evens = ", ".join([str(n) for n in even_nums])
odds = ", ".join([str(n) for n in odd_nums])
print(f"Positive: {positives}")
print(f"Negative: {negatives}")
print(f"Even: {evens}")
print(f"Odd: {odds}")