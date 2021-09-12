command = input()
total_price = 0

while not command == "special" and not command == "regular":

    part_price = float(command)
    if part_price <= 0:
        print("Invalid price!")

    else:
        total_price += part_price

    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    final_price = total_price + taxes
    if command == "special":
        final_price *= 0.9
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_price:.2f}$")


