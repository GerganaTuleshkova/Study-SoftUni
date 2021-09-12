import re
pattern_product = r"^@\#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@\#+$"
pattern_numbers = r"\d"

products = []
num_of_texts = int(input())
for n in range(num_of_texts):
    text = input()
    product_found = re.search(pattern_product, text)
    product_group = ""
    if product_found:
        digits_found = re.findall(pattern_numbers, product_found.string)
        for digit in digits_found:
            product_group += digit
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")






