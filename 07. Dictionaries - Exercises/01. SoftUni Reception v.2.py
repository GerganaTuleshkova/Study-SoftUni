employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())
students = int(input())

total_efficiency_per_hour = employee_1_efficiency + employee_2_efficiency + employee_3_efficiency
hours = 0

while students > 0:
    hours += 1
    if not hours % 4 == 0:
        students -= total_efficiency_per_hour

print(f"Time needed: {hours}h.")