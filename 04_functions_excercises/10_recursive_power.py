def recursive_power(number, power):
    # return number ** power

    if power == 1:
        return number

    result = number * recursive_power(number, power - 1)
    return result

print(recursive_power(2, 10))