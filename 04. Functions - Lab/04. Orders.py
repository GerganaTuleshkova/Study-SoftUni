def calculate_total_price(product, count):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00
    return price * count


product_ordered = input()
number_of_products = int(input())
print(f"{calculate_total_price(product_ordered,number_of_products):.2f}")
