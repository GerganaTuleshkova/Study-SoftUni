def even_odd(*args):
    criteria = args[-1]
    if criteria == "odd":
        result = [n for n in args[:-1] if n % 2 != 0]
    elif criteria == "even":
        result = [n for n in args[:-1] if n % 2 == 0]
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


