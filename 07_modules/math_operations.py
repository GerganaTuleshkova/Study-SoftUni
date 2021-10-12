def do_math_operation(number1, number2, operator):
    if operator == "+":
        return number1 * number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "^":
        return number1 ** number2
    elif operator == "/":
        if number2 == 0:
            raise ValueError("Divisor cannot be 0.")
        return number1 / number2