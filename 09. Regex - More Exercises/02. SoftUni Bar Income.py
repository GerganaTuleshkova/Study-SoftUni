import re

text = input()
pattern = r"\.*%(?P<client_name>[A-Z][a-z]+)%.*<(?P<product_name>\w+)>.*\|(?P<quantity>\d+)\|\D*(?P<price>\d+(\.\d+)*)\$"
#pattern = r"\.*%(?P<client_name>[A-Z][a-z]+)%\.*<(?P<product_name>\w+)>\.*\|(?P<quantity>\d+)\|\.*(?P<price>\d+\.\d+)\$
total_income = 0

while not text == "end of shift":
    purchase_info = re.finditer(pattern, text)
    for info in purchase_info:
        client_name = info.group("client_name")
        product = info.group("product_name")
        quantity = int(info.group("quantity"))
        price = float(info.group("price"))
        print(f"{client_name}: {product} - {(quantity * price):.2f}")
        total_income += quantity * price

    text = input()

print(f"Total income: {total_income:.2f}")