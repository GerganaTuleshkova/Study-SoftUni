def calculate(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return int(num_1 / num_2)
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2


operator_given = input()
first_num = int(input())
second_num = int(input())
print(calculate(operator_given, first_num, second_num))