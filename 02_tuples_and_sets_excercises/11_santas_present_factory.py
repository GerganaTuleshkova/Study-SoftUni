from collections import deque


def toy_is_crafted(magic):
    toy = ""
    if magic == 150:
        toy = "Doll"
    elif magic == 250:
        toy = "Wooden train"
    elif magic == 300:
        toy = "Teddy bear"
    elif magic == 400:
        toy = "Bicycle"
    return toy


materials_stack = [int(n) for n in input().split()]
magic_levels_queue = deque([int(n) for n in input().split()])

toys_made = {}

while materials_stack and magic_levels_queue:
    current_material = materials_stack[-1]
    current_magic_level = magic_levels_queue[0]
    current_magic = current_magic_level * current_material
    toy = toy_is_crafted(current_magic)
    if toy != "":
        if toy not in toys_made:
            toys_made[toy] = 0
        toys_made[toy] += 1
        materials_stack.pop()
        magic_levels_queue.popleft()
    else:
        if current_magic < 0:
            addition = current_magic_level + current_material
            materials_stack.pop()
            magic_levels_queue.popleft()
            materials_stack.append(addition)
        elif current_magic > 0:
            magic_levels_queue.popleft()
            materials_stack[-1] += 15
        else:
            if current_magic_level == 0:
                magic_levels_queue.popleft()
            if current_material == 0:
                materials_stack.pop()

if ("Teddy bear" in toys_made and "Bicycle" in toys_made) or ("Doll" in toys_made and "Wooden train" in toys_made):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print(f"Materials left: {', '.join([str(n) for n in materials_stack[::-1]])}")

if magic_levels_queue:
    print(f"Magic left: {', '.join([str(n) for n in magic_levels_queue])}")

for toy_name, toy_count in sorted(toys_made.items()):
    print(f"{toy_name}: {toy_count}")