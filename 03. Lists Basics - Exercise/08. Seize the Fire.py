string_fires_and_cells = input()
water = int(input())
fires_and_cells_list = string_fires_and_cells.split("#")
effort = 0
cells_put_out = []

for item in fires_and_cells_list:
    f_c = item.split(" = ")
    cell_value = int(f_c[1])
    if f_c[0] == "High":
        if cell_value < 81 or cell_value > 125:
            continue
        else:
            if water < cell_value:
                continue
            else:
                water -= cell_value
                effort += cell_value * 0.25
                cells_put_out.append(cell_value)
    if f_c[0] == "Medium":
        if cell_value < 51 or cell_value > 80:
            continue
        else:
            if water < cell_value:
                continue
            else:
                water -= cell_value
                effort += cell_value * 0.25
                cells_put_out.append(cell_value)
    if f_c[0] == "Low":
        if cell_value < 1 or cell_value > 50:
            continue
        else:
            if water < cell_value:
                continue
            else:
                water -= cell_value
                effort += cell_value * 0.25
                cells_put_out.append(cell_value)

print("Cells:")
for cell in cells_put_out:
    print(f"- {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells_put_out)}")

