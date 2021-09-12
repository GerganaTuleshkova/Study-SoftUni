command = input()

dwarfs_by_name = {}
colours = {}

while not command == "Once upon a time":
    info = command.split(" <:> ")
    name, hat_color, physics = info[0], info[1], int(info[2])

    name_hat_pair = f"{name}:{hat_color}"
    if name_hat_pair not in dwarfs_by_name:
        dwarfs_by_name[name_hat_pair] = [hat_color, physics, name]
        if hat_color not in colours:
            colours[hat_color] = 1
        else:
            colours[hat_color] += 1
    else:
        if dwarfs_by_name[name_hat_pair][1] < physics:
            dwarfs_by_name[name_hat_pair][1] = physics

    command = input()

ordered_dwarfs = dict(sorted(dwarfs_by_name.items(), key=lambda kvp: -kvp[1][1]))


dwarf_dict_plus_count = ordered_dwarfs.copy()
for key in dwarf_dict_plus_count:
    hat_color = dwarf_dict_plus_count[key][0]

    dwarf_dict_plus_count[key].append(colours[hat_color])

for k, v in sorted(dwarf_dict_plus_count.items(), key=lambda x: (-x[1][1], -x[1][3])):
    print(f"({v[0]}) {v[2]} <-> {v[1]}")