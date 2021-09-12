import re

#pattern_barcode = r"^(?P<surrounding>@#+)(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])(?P=surrounding)$"
pattern_barcode = r"^(?P<surrounding>@#+)(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])@#+$"
pattern_digits = r"\d"

count_of_barcodes = int(input())

for n in range(count_of_barcodes):
    text = input()
    barcode_match_obj = re.fullmatch(pattern_barcode, text)
    if not barcode_match_obj:
        print("Invalid barcode")
    else:
        barcode = barcode_match_obj.group("barcode")
        group_as_list = re.findall(pattern_digits, barcode)

        # group_as_list = [char for char in barcode if char.isdigit()]

        if not group_as_list:
            print("Product group: 00")
        else:
            product_group = ""
            for digit_as_str in group_as_list:
                product_group += digit_as_str

            #product_group = "".join(group_as_list)

            print(f"Product group: {product_group}")


