foods = input().split()
my_foods = {}

for index in range(0, len(foods), 2):
    key = foods[index]
    value = int(foods[index +1])
    my_foods[key] = value

print(my_foods)
