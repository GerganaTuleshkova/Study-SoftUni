command = input()
courses = {}

while not command == "end":
    info = command.split(" : ")
    course, student = info[0], info[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    command = input()

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for c, students in courses.items():
    print(f"{c}: {len(students)}")
    for s in sorted(students):
        print(f"-- {s}")