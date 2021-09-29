def operate(operator, *args):
    result = args[0]
    if operator == "+":

        for el in args[1:]:
            result += el
    elif operator == "-":

        for el in args[1:]:
            result -= el
    elif operator == "*":

        for el in args[1:]:
            result *= el
    elif operator == "/":

        for el in args[1:]:
            if el != 0:
                result /= el
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

