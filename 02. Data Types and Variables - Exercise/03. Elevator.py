from math import ceil

number_of_people = int(input())
capacity = int(input())

cources = ceil(number_of_people / capacity)
print((cources))