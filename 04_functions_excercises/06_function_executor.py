def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    results = []
    for function, parameters in args:
        current_result = function(*parameters)
        results.append(current_result)
    return results


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
