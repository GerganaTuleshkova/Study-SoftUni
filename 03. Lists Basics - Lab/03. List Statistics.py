number_of_lines = int(input())

positive_nums = []
negative_nums = []

for _ in range(number_of_lines):
    given_number = int(input())
    if given_number >= 0:
        positive_nums.append(given_number)
    else:
        negative_nums.append(given_number)

print(positive_nums)
print(negative_nums)
print(f"Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}")