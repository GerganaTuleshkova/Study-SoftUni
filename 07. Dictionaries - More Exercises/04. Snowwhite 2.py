command = input()

dwarfs_by_name = {}
colours = {}

while not command == "Once upon a time":
    info = command.split(" <:> ")
    name, hat_color, physics = info[0], info[1], int(info[2])

    key = f"{name}:{hat_color}"
    if key not in dwarfs_by_name:
        dwarfs_by_name[key] = [hat_color, physics]
        if hat_color not in colours:
            colours[hat_color] = 1
        else:
            colours[hat_color] += 1
    else:
        if dwarfs_by_name[key][1] < physics:
            dwarfs_by_name[key][1] = physics

    command = input()

dwarfs_by_physics = {}
#
# for dwarf_name, details in dwarfs_by_name.items():
#     for h_color, d_physics in details.items():
#         if d_physics not in dwarfs_by_physics:
#             dwarfs_by_physics[d_physics] = {}
#             dwarfs_by_physics[d_physics].update({h_color: []})
#             # dwarfs_by_physics[d_physics][h_color] = []
#             dwarfs_by_physics[d_physics][h_color].append(dwarf_name)
#         else:
#             if h_color not in dwarfs_by_physics[d_physics]:
#                 dwarfs_by_physics[d_physics][h_color] = [dwarf_name]
#             else:
#                 dwarfs_by_physics[d_physics][h_color] += [dwarf_name]
# print(dwarfs_by_physics)
# dwarfs_by_physics = dict(sorted(dwarfs_by_physics.items(), key=lambda x: (-(x[0]),)))
# print(dwarfs_by_name)
# print(dwarfs_by_physics)
#
# for p, hats_and_names in dwarfs_by_physics.items():
#     for hat, names_list in (sorted(hats_and_names.items(), key=lambda x: -(len(x[1])))):
#         for name in (names_list):
#             print(f"({hat}) {name} <-> {p}")

print(dwarfs_by_name)

