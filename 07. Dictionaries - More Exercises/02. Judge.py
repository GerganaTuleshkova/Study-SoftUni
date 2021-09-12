def thing_in_dict_keys(given_dict, searched_word):
    if searched_word in given_dict:
        return True
    return False


stats_by_contest = {}
stats_by_user = {}

command = input()

while not command == "no more time":
    info = command.split(" -> ")
    username, contest, points = info[0], info[1], int(info[2])
    if not thing_in_dict_keys(stats_by_contest, contest):
        stats_by_contest[contest] = {}
        stats_by_contest[contest][username] = points
    else:
        if username not in stats_by_contest[contest]:
            stats_by_contest[contest][username] = points
        else:
            # the user has already taken the test, check the previous result
            if points > stats_by_contest[contest][username]:
                stats_by_contest[contest][username] = points

    if not thing_in_dict_keys(stats_by_user, username):
        stats_by_user[username] = {}
        stats_by_user[username][contest] = points
    else:
        if contest not in stats_by_user[username]:
            stats_by_user[username][contest] = points
        else:
            if points > stats_by_user[username][contest]:
                stats_by_user[username][contest] = points
    command = input()

# print(stats_by_contest)
# print(stats_by_user)

for test, user_stat in stats_by_contest.items():
    print(f"{test}: {len(user_stat)} participants")
    position = 0
    for user_name, user_score in (sorted(user_stat.items(), key=lambda x: (-(x[1]), (x[0])))):
        position += 1
        print(f"{position}. {user_name} <::> {user_score}")

print("Individual standings:")
users_total_score = {}
for user, contest_result in stats_by_user.items():
    users_total_score[user] = 0
    for score_on_test in contest_result.values():
        users_total_score[user] += score_on_test

# print(users_total_score)
position_2 = 0
for user, total_score in (sorted(users_total_score.items(), key=lambda x: (-(x[1]), x[0]))):
    position_2 += 1
    print(f"{position_2}. {user} -> {total_score}")