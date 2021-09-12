command = input()
students = {}
while ":" in command:
    student_info = command.split(":")
    name, id_num, course = student_info[0], int(student_info[1]), student_info[2]
    if course not in students:
        students[course] = {}
    students[course][id_num] = name
    command = input()

searched_course = " ".join(command.split("_"))
if searched_course in students:
    for key, value in students[searched_course].items():
        print(f"{value} - {key}")


