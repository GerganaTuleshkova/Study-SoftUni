command = input()
results = {}

while not command == "exam finished":
    info = command.split("-")
    name, language = info[0], info[1]
    if not language == "banned":
        points = int(info[2])
        if language not in results:
            results[language] = []
        results[language].append(name)
        results[language].append(points)
    else:
        for lang in results:
            if name in results[lang]:
                for i in range(0, len(results[lang])-1, 2):
                    if results[lang][i] == name:
                        results[lang][i+1] = -1

    command = input()


best_results = []
for key, student in results.items():
    best_results += student

highest_results = {}
for i in range(0, len(best_results), 2):
    if best_results[i] not in highest_results and best_results[i + 1] != -1:
        highest_results[best_results[i]] = best_results[i + 1]
    elif best_results[i] in highest_results:
        if best_results[i+1] >= highest_results[best_results[i]]:
            highest_results[best_results[i]] = best_results[i+1]

highest_results = dict(sorted(highest_results.items()))
highest_results = dict(sorted(highest_results.items(), key=lambda x: -x[1]))
# print(best_results)
# print(highest_results)

print("Results:")
for k, v in highest_results.items():
    print(f"{k} | {v}")

print("Submissions:")
results_by_submission = dict(sorted(results.items(), key=lambda x: -len(x[1])))
for key, value in results_by_submission.items():
    print(f"{key} - {int(len(value)/2)}")