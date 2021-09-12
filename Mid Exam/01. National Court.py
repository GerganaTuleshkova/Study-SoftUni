employee_1_capacity_per_hour = int(input())
employee_2_capacity_per_hour = int(input())
employee_3_capacity_per_hour = int(input())
total_people = int(input())
capacity_per_hour = employee_1_capacity_per_hour + employee_2_capacity_per_hour + employee_3_capacity_per_hour

hours_count = 0

while total_people > 0:
    hours_count += 1
    if hours_count % 4 == 0:
        continue
    else:
        total_people -= capacity_per_hour

print(f"Time needed: {hours_count}h.")