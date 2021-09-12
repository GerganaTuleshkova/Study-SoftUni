command = input()
products = {}

while not command == "buy":
    info = command.split()
    beverage, price, quantity = info[0], float(info[1]), int(info[2])
    if beverage not in products:
        products[beverage] = [0, 0]
    products[beverage][0] = price
    products[beverage][1] += quantity

    command = input()

for product, pr_info in products.items():
    print(f"{product} -> {(pr_info[0] * pr_info[1]):.2f}")