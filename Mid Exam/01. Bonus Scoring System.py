from math import ceil

student_number = int(input())
lectures_in_course = int(input())
additional_bonus = int(input())

max_bonus = 0
attendance_of_max_bonus_student = 0

for s in range(student_number):
    attendance = int(input())
    bonus_of_student = ceil(attendance / lectures_in_course * (5 + additional_bonus))
    if bonus_of_student >= max_bonus:
        max_bonus = bonus_of_student
        attendance_of_max_bonus_student = attendance

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {attendance_of_max_bonus_student} lectures.")
