def stock_availability(inventory: list, action, *args):

    if action == "delivery":
        for box in args:
            inventory.append(box)
    if action == "sell":
        if not args:
            inventory.pop(0)
        elif isinstance(args[0], int):

            boxes_to_remove = min(args[0], len(inventory))

            for _ in range(boxes_to_remove):
                inventory.pop(0)
        else:
            for box in args:
                #if box in inventory:
                    # while box in inventory:
                    #     inventory.remove(box)
                while box in inventory:
                    inventory.remove(box)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
