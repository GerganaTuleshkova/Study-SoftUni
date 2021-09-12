def is_valid_contest(contests_list: dict, searched_contest: str):
    if searched_contest in contests_list.keys():
        return True
    return False


def is_user_not_in_contest(results_list: dict, user, contest):
    user_not_in_contest = True
    for user_info_index in range(len(results_list[contest])):
        if user in results_list[contest][user_info_index]:
            user_not_in_contest = False
            return False
    if user_not_in_contest:
        return True


contests_passwords = {}
rankings_by_contest = {}
rankings_by_user = {}
command = input()

while not command == "end of contests":
    info = command.split(":")
    contest, password = info[0], info[1]
    contests_passwords[contest] = password
    command = input()

command_2 = input()

for key in contests_passwords:
    rankings_by_contest[key] = []

while not command_2 == "end of submissions":
    info_2 = command_2.split("=>")
    contest, password_provided, username, points = info_2[0], info_2[1], info_2[2], int(info_2[3])
    if is_valid_contest(contests_passwords, contest) and password_provided == contests_passwords[contest]:
        if is_user_not_in_contest(rankings_by_contest, username, contest):
            rankings_by_contest[contest].append([])
            rankings_by_contest[contest][-1].append(username)
            rankings_by_contest[contest][-1].append(points)
        else:
            for mini_list_index in range(len(rankings_by_contest[contest])):
                if username in rankings_by_contest[contest][mini_list_index]:
                    user_list_index = mini_list_index
            if points > rankings_by_contest[contest][user_list_index][1]:
                rankings_by_contest[contest][user_list_index][1] = points
        if username not in rankings_by_user:
            rankings_by_user[username] = {}
            rankings_by_user[username][contest] = points

        else:
            if contest in rankings_by_user[username]:
                if points > rankings_by_user[username][contest]:
                    rankings_by_user[username][contest] = points
            else:
                rankings_by_user[username][contest] = points

    command_2 = input()

results_and_names = {}
for students_info_list in rankings_by_contest.values():
    for i in range(len(students_info_list)):
        student_name = students_info_list[i][0]
        student_score = students_info_list[i][1]
        if student_name not in results_and_names:
            results_and_names[student_name] = 0
        results_and_names[student_name] += student_score


orderred_candidates = sorted(results_and_names.items(), key=lambda x: -(x[1]))
print(f"Best candidate is {orderred_candidates[0][0]} with total {orderred_candidates[0][1]} points.")

print("Ranking:")
for key, value in sorted(rankings_by_user.items()):
    print(f"{key}")
    ordered_contest_result_of_user = sorted(value.items(), key=lambda x: -(x[1]))

    for contest_result in ordered_contest_result_of_user:
        print(f"#  {contest_result[0]} -> {contest_result[1]}")