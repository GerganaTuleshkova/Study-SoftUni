import re

given_text = input()
pattern = r"(?P<product>(?<=>>)[a-zA-z]+)<<(?P<price>\d+(\.\d+)*)!(?P<quantity>\d+)"
products_purchased = []
total_spend = 0
while not given_text == "Purchase":
    current_purchase = re.search(pattern, given_text)

    if current_purchase:
        products_purchased.append(current_purchase.group("product"))
        total_spend += float(current_purchase.group("price"))* int(current_purchase.group("quantity"))

    given_text = input()

print("Bought furniture:")
for product in products_purchased:
    print(product)
print(f"Total money spend: {total_spend:.2f}")