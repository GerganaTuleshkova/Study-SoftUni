def multiply_string(string, counter):
    return string * counter


given_string = input()
counter_given = int(input())
print(multiply_string(given_string, counter_given))

calc = lambda a, b: a * b
result = calc(given_string, counter_given)
print(result)