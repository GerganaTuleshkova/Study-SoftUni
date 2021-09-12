num_of_lines = int(input())
health_default = 250
damage_default = 45
armor_default = 10

dragons_dict = {}
types_stats = {}

for n in range(num_of_lines):
    info = input().split()
    type_dragon, name, damage, health, armor = info[0], info[1], info[2], info[3], info[4]
    if damage == "null":
        damage = damage_default
    else:
        damage = int(damage)
    if health == "null":
        health = health_default
    else:
        health = int(health)
    if armor == "null":
        armor = armor_default
    else:
        armor = int(armor)
    name_type_pair = f"{name}:{type_dragon}"
    dragons_dict[name_type_pair] = {"name": name, "type": type_dragon, "damage": damage, "health": health, "armor": armor}
    if type_dragon not in types_stats:
        types_stats[type_dragon] = {"names": [name]}
    else:
        if name not in types_stats[type_dragon]["names"]:
            types_stats[type_dragon]["names"].append(name)

for t, values in types_stats.items():
    types_stats[t]["damages_all"] = []
    types_stats[t]["health_all"] = []
    types_stats[t]["armors_all"] = []
    for key, dragon_details_dict in dragons_dict.items():
        if dragon_details_dict["type"] == t:

            types_stats[t]["damages_all"].append(dragon_details_dict["damage"])
            types_stats[t]["health_all"].append(dragon_details_dict["health"])
            types_stats[t]["armors_all"].append(dragon_details_dict["armor"])


for typ, val in types_stats.items():
    average_damage = sum(val["damages_all"])/ len(val["damages_all"])
    average_health = sum(val["health_all"])/ len(val["health_all"])
    average_armor = sum(val["armors_all"])/ len(val["armors_all"])
    print(f"{typ}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for dr_typ_pair, valu in sorted(dragons_dict.items()):
        if valu["type"] == typ:
            print(f"-{valu['name']} -> damage: {valu['damage']}, health: {valu['health']}, armor: {valu['armor']}")




