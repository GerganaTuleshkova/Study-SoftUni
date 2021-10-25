def shopping_list(budget: int, **kwargs):
    if budget < 100:
        return "You do not have enough budget."
    types_purchased = 0
    result_message = ""

    for product_name, product_details in kwargs.items():
        required_money = product_details[0] * product_details[1]
        if budget >= required_money:
            current_message = f"You bought {product_name} for {required_money:.2f} leva.\n"
            result_message += current_message
            types_purchased += 1
            budget -= required_money

        if types_purchased >= 5:
            break
    return result_message




print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


# (shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# (shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
# (shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
