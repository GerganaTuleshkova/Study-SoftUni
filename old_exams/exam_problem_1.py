from collections import deque

materials_stack = [int(x) for x in input().split()]
magic_level_queue = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0}

crafting_ready = False

while materials_stack and magic_level_queue:
    current_material = materials_stack.pop()
    current_magic = magic_level_queue.popleft()
    sum = current_material + current_magic
    if sum < 100 and sum % 2 == 0:
        sum = current_material * 2 + current_magic * 3
    elif sum < 100 and not sum % 2 == 0:
        sum *= 2

    if sum > 499:
        sum /= 2

    if 100 <= sum <= 199:
        presents["Gemstone"] += 1
    elif 200 <= sum <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= sum <= 399:
        presents["Gold"] += 1
    elif 400 <= sum <= 499:
        presents["Diamond Jewellery"] += 1


if (presents["Gemstone"] >= 1 and presents["Porcelain Sculpture"] >= 1) \
        or (presents["Gold"] >= 1 and presents["Diamond Jewellery"] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials_stack:
    print(f"Materials left: {', '.join([str(x) for x in materials_stack])}")

if magic_level_queue:
    print(f"Magic left: {', '.join([str(x) for x in magic_level_queue])}")

for present_type, count in sorted(presents.items()):
    if count >= 1:
        print(f"{present_type}: {count}")