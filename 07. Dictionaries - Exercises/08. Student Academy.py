num_pairs = int(input())
academy = {}

for p in range(num_pairs):
    student_name = input()
    grade = float(input())
    if student_name not in academy:
        academy[student_name] = []
    academy[student_name].append(grade)

above_average = {key: (sum(grades)/len(grades)) for (key, grades) in academy.items() if (sum(grades)/len(grades)) >= 4.50}
above_average = dict(sorted(above_average.items()))

above_average = dict(sorted(above_average.items(), key=lambda x: -x[1]))


for s, g in above_average.items():
    print(f"{s} -> {g:.2f}")