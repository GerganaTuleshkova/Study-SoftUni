from math_operations import do_math_operation

number1, operator, number2 = input().split()
number1 = float(number1)
number2 = float(number2)

try:
    print(f"{do_math_operation(number1, number2, operator):.2f}")
except ValueError as err:
    print(err)