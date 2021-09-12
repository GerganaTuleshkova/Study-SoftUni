text = input()
materials = {}

while not text == "stop":
    metal = text
    quantity = int(input())
    if metal not in materials:
        materials[metal] = 0
    materials[metal] += quantity

    text = input()

for m, q in materials.items():
    print(f"{m} -> {q}")