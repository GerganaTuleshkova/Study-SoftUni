num_of_heroes_to_choose = int(input())
heroes_details = {}

for n in range(num_of_heroes_to_choose):
    info = input()
    info = info.split()
    hero_name = info[0]
    hit_points = int(info[1])
    mana_points = int(info[2])
    heroes_details[hero_name] = {"hp":hit_points, "mp": mana_points}

command = input()

while not command == "End":
    info_actions = command.split(" - ")
    action, hero = info_actions[0], info_actions[1]
    if action == "CastSpell":
        mp_needed = int(info_actions[2])
        spell_name = info_actions[3]
        if heroes_details[hero]["mp"] >= mp_needed:
            heroes_details[hero]["mp"] -= mp_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_details[hero]['mp'] } MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(info_actions[2])
        attacker = info_actions[3]
        heroes_details[hero]["hp"] -= damage
        if heroes_details[hero]["hp"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_details[hero]['hp']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes_details[hero]
    elif action == "Recharge":
        amount = int(info_actions[2])
        if amount + heroes_details[hero]["mp"] > 200:
            amount = 200 - heroes_details[hero]["mp"]
        heroes_details[hero]["mp"] += amount
        print(f"{hero} recharged for {amount} MP!")
    elif action == "Heal":
        amount_hp = int(info_actions[2])
        if amount_hp + heroes_details[hero]["hp"] > 100:
            amount_hp = 100 - heroes_details[hero]["hp"]
        heroes_details[hero]["hp"] += amount_hp
        print(f"{hero} healed for {amount_hp} HP!")

    command = input()

ordered_heroes = sorted(heroes_details.items(), key=lambda tkvp: (-tkvp[1]['hp'], tkvp[0]))

for hero_n, hero_detail_dict in ordered_heroes:
    print(f"{hero_n}")
    print(f"  HP: {hero_detail_dict['hp']}")
    print(f"  MP: {hero_detail_dict['mp']}")
