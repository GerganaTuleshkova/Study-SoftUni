materials = {"shards": 0, "fragments": 0, "motes": 0}
key_materials = ["shards", "fragments", "motes"]
limit_reached = False
while limit_reached == False:
    info = input().split()
    # material, quantity = info[1], int(info[0])
    for index in range(0, len(info), 2):
        quantity = int(info[index])
        material = info[index + 1].lower()
        if material not in materials:
            materials[material] = 0
        materials[material] += quantity
        if material in key_materials and materials[material] >= 250:
            materials[material] -= 250
            limit_reached = True
            legendary_item = ""
            if material == "shards":
                legendary_item = "Shadowmourne"
            elif material == "fragments":
                legendary_item = "Valanyr"
            elif material == "motes":
                legendary_item = "Dragonwrath"
            print(f"{legendary_item} obtained!")
            break

key_m_only = {key: value for (key, value) in materials.items() if key in key_materials}
key_m_only = dict(sorted(key_m_only.items()))
key_m_only = dict(sorted(key_m_only.items(), key=lambda x: -x[1]))

junk = {key: value for (key, value) in materials.items() if key not in key_materials}
junk = dict(sorted(junk.items()))


for k, v in key_m_only.items():
    print(f"{k}: {v}")

for k, v in junk.items():
    print(f"{k}: {v}")
