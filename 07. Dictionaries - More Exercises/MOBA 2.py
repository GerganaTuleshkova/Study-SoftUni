def is_player_in_pool(pool: dict, player):
    if player in pool.keys():
        return True
    return False


def battle(pool, player1, player2, result_pool):
    if is_player_in_pool(pool, player1) and is_player_in_pool(pool, player2):
        compared_skills_player_1 = 0
        compared_skills_player_2 = 0
        for player1_position in pool[player1].keys():
            for player2_position in pool[player2].keys():
                if player2_position == player1_position:
                    compared_skills_player_1 += pool[player1][player1_position]
                    compared_skills_player_2 += pool[player2][player2_position]

        if compared_skills_player_1 > compared_skills_player_2:
            if player2 in result_pool:
                result_pool.pop(player2, None)
        elif compared_skills_player_1 < compared_skills_player_2:
            if player2 in result_pool:
                result_pool.pop(player1, None)
    return result_pool


command = input()
players_pool = {}
total_skill_per_player = {}
# All players with their skills are added to the pool
# (dict where key is player name and each player name has a dict position:skill
while " -> " in command:
    info = command.split(" -> ")
    player, position, skill = info[0], info[1], int(info[2])
    if not is_player_in_pool(players_pool, player):
        players_pool[player] = {}
        players_pool[player][position] = skill
        total_skill_per_player[player] = skill
    else:
        if position not in players_pool[player]:
            players_pool[player][position] = skill
            total_skill_per_player[player] += skill
        else:
            if skill >= players_pool[player][position]:
                total_skill_per_player[player] += skill - players_pool[player][position]
                players_pool[player][position] = skill

    command = input()

results_pool = players_pool.copy()

while not command == "Season end":
    info_match = command.split(" vs ")
    player_1, player_2 = info_match[0], info_match[1]
    results_pool = battle(players_pool, player_1, player_2, results_pool)

    players_pool = results_pool.copy()
    command = input()

total_skills = {}
for player_left, player_results in players_pool.items():
    if not is_player_in_pool(total_skills, player_left):
        total_skills[player_left] = 0
    for result in player_results.values():
        total_skills[player_left] += result
total_skills = dict(sorted(total_skills.items(), key=lambda x: (-(x[1]), x[0])))

for player, total_skill in total_skills.items():
    print(f"{player}: {total_skill} skill")
    for position, skill in (sorted(players_pool[player].items(), key=lambda x: (-(x[1]), x[0]))):
        print(f"- {position} <::> {skill}")
