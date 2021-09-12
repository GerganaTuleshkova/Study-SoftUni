foods = input().split()
my_foods = {}

for index in range(0, len(foods), 2):
    key = foods[index]
    value = int(foods[index +1])
    my_foods[key] = value

searched_products = input().split()

for product in searched_products:
    if product in my_foods.keys():
        print(f"We have {my_foods[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")