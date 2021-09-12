import re

pattern_barcode = r"^(?P<surrounding>@#+)(?P<barcode>[A-Z][a-zA-Z0-9]{4,}[A-Z])(?P=surrounding)$"
barcodes = []
count_of_barcodes = int(input())

for n in range(count_of_barcodes):
    text = input()
    group = ""
    barcode_match_obj = re.fullmatch(pattern_barcode, text)
    if not barcode_match_obj:
        print("Invalid barcode")
    else:
        barcode = barcode_match_obj.group("barcode")
        print(barcode)
        group_as_list = [char for char in barcode if char.isdigit()]
        print(group_as_list)
        if not group_as_list:
            print("Product group: 00")
        else:
            product_group = "".join(group_as_list)
            print(f"Product group: {product_group}")


