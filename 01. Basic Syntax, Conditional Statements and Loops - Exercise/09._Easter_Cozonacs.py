budget = float(input())
flour_price_1kg = float(input())
eggs_price_pack = flour_price_1kg * 0.75
milk_price_l = flour_price_1kg * 1.25
colored_eggs = 0
cozonac_cost = flour_price_1kg + eggs_price_pack + milk_price_l *0.25
number_of_cosonacs = 0

while budget > cozonac_cost:
    budget -= cozonac_cost
    number_of_cosonacs += 1
    colored_eggs += 3
    if number_of_cosonacs % 3 == 0:
        colored_eggs -= (number_of_cosonacs - 2)

print(f"You made {number_of_cosonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")