quantity = int(input())
days = int(input())

total_cost = 0
gained_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

if days % 10 == 0:
    gained_spirit -= 30

for day in range(1, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set_price*quantity
        gained_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skirt_price + tree_garland_price) * quantity
        gained_spirit += 13
    if day % 5 == 0:
        total_cost += (tree_lights_price * quantity)
        gained_spirit += 17
        if day % 3 == 0:
            gained_spirit += 30
    if day % 10 == 0:
        gained_spirit -= 20
        total_cost += tree_lights_price + tree_garland_price + tree_skirt_price
    #
    # if day % 11 == 0:
    #     quantity += 2

print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")

