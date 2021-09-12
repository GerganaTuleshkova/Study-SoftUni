needed_experience = float(input())
battles_count = int(input())
collected_experience = 0

goal_reached = False
for battle in range(1, battles_count + 1):
    experience = float(input())
    if battle % 3 == 0:
        experience *= 1.15
    if battle % 5 == 0:
        experience *= 0.9
    if battle % 15 == 0:
        experience *= 1.05
    collected_experience += experience
    if collected_experience >= needed_experience:
        goal_reached = True
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

if not goal_reached:
    print(f"Player was not able to collect the needed experience, {(needed_experience - collected_experience):.2f} more needed.")
