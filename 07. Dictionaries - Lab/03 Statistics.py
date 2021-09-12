products = {}

command = input()
while not command == "statistics":
    info = command.split(":")
    key, value = info[0], int(info[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value
    command = input()

print("Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")