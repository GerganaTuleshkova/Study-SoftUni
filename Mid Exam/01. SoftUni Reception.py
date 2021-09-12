employee_1_capacity = int(input())
employee_2_capacity = int(input())
employee_3_capacity = int(input())

total_capacity_per_hour = employee_1_capacity + employee_2_capacity + employee_3_capacity

students_count = int(input())
hours = 0

while students_count > 0:
    hours += 1
    if not hours % 4 == 0:
        students_count -= total_capacity_per_hour

print(f"Time needed: {hours}h.")