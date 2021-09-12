team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
cards = input()

cards_list = cards.split(" ")
game_terminated = False

for element in cards_list:
    if "A" in element:
        player = int(element[2:])
        if player in team_A:
            team_A.remove(player)
        if len(team_A) < 7:
            game_terminated = True
            break
    elif "B" in element:
        player = int(element[2:])
        if player in team_B:
            team_B.remove(player)
        if len(team_B) < 7:
            game_terminated = True
            break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if game_terminated:
    print("Game was terminated")