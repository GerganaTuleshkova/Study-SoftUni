plants_rarity = {}
plants_ratings = {}
plant_average_rating = {}
num_of_plants = int(input())

for n in range(num_of_plants):
    plant_info = input().split("<->")
    name, rarity = plant_info[0], int(plant_info[1])
    plants_rarity[name] = rarity
    plants_ratings[name] = []

command = input()

while not command == "Exhibition":
    info = command.split(": ")
    action = info[0]
    detailed_info = info[1].split(" - ")
    plant = detailed_info[0]
    if action == "Rate":
        rating = int(detailed_info[1])
        if plant not in plants_rarity:
            print("error")
        else:
            plants_ratings[plant].append(rating)
    elif action == "Update":
        new_rarity = int(detailed_info[1])
        if plant not in plants_rarity:
            print("error")
        else:
            plants_rarity[plant] = new_rarity
    elif action == "Reset":
        if plant not in plants_rarity:
            print("error")
        else:
            plants_ratings[plant] = []

    command = input()


for pl, ratings_list in plants_ratings.items():
    if len(ratings_list) > 0:
        plant_average_rating[pl] = sum(ratings_list) / len(ratings_list)
    else:
        plant_average_rating[pl] = 0.00


plant_all_dict = {}
for k, v in plants_rarity.items():
    plant_all_dict[k] = {"rarity": v, "av_rating": plant_average_rating[k]}


ordered_plants = sorted(plant_all_dict.items(), key=lambda tkvp: (-tkvp[1]["rarity"], -tkvp[1]["av_rating"]))

print("Plants for the exhibition:")

for k, v in ordered_plants:
    print(f"- {k}; Rarity: {v['rarity']}; Rating: {v['av_rating']:.2f}")