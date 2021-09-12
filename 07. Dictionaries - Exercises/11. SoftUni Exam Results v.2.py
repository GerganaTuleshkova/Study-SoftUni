command = input()
results = {}

while not command == "exam finished":
    info = command.split("-")
    name, language = info[0], info[1]
    if not language == "banned":
        points = int(info[2])
        if language not in results:
            results[language] = []
        results[language].append([])
        results[language][-1].append(name)
        results[language][-1].append(points)
    else:
        for lang in results:
            for i in range(len(results[lang])):
                if name in results[lang][i]:
                    results[lang][i][1] = -1

    command = input()


all_results = []
for key, student in results.items():
    all_results += student



highest_results = {}
for i in range(0, len(all_results)):
    student_name, student_result = all_results[i][0], all_results[i][1]
    if student_name not in highest_results and student_result != -1:
        highest_results[student_name] = student_result
    elif student_name in highest_results:
        if student_result >= highest_results[student_name]:
            highest_results[student_name] = student_result

orderred_highest_results = (sorted(highest_results.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for k, v in orderred_highest_results:
    print(f"{k} | {v}")

print("Submissions:")
results_by_submission = (sorted(results.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in results_by_submission:
    print(f"{key} - {int(len(value))}")