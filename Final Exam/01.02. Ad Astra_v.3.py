import re
from math import floor

text = input()

pattern = r"(?P<separator>[\#\|])(?P<name>[a-zA-Z\s]+)(?P=separator)(?P<exp_date>[0-3]\d\/[0-1]\d\/\d{2})(?P=separator)(?P<calories>\d{1,4})(?P=separator)"
# pattern = r"(?P<separator>[\#\|])(?P<name>[A-Z( )*a-z]+)(?P=separator)(?P<exp_date>[0-3]\d\/[0-1]\d\/\d{2})(?P=separator)(?P<calories>\d{1,5})(?P=separator)"
day_need = 2000
food_dict = {}
total_calories = 0

foods_iter = re.finditer(pattern, text)
for match in foods_iter:
    food = match.group("name")
    expiration_date = match.group("exp_date")
    calories = int(match.group("calories"))
    total_calories += calories
    food_dict[food] = [expiration_date, calories]

print(f"You have food to last you for: {int(total_calories // day_need)} days!")

for food_name, food_details in food_dict.items():
    print(f"Item: {food_name}, Best before: {food_details[0]}, Nutrition: {food_details[1]}")







