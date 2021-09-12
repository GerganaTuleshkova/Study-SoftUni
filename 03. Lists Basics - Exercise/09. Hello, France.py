string_items = input()
budget = float(input())

items_list = string_items.split("|")
items_bought = []
total_spend = 0
for pair in items_list:
    pair_list = pair.split("->")
    type_item = pair_list[0]
    price = float(pair_list[1])
    if type_item == "Clothes":
        if price > 50:
            continue
        else:
            if budget >= price:
                budget -= price
                items_bought.append(price * 1.40)
            else:
                continue
    if type_item == "Shoes":
        if price > 35:
            continue
        else:
            if budget >= price:
                budget -= price
                items_bought.append(price * 1.40)

            else:
                continue
    if type_item == "Accessories":
        if price > 20.50:
            continue
        else:
            if budget >= price:
                budget -= price
                items_bought.append(price * 1.40)

            else:
                continue

for p in items_bought:
    print(f"{p:.2f}", end=" ")

profit = sum(items_bought)*0.4/1.40
print(f"\nProfit: {profit:.2f}")

if (sum(items_bought) + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")