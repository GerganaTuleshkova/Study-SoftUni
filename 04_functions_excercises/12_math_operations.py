def math_operations(*args, **kwargs):
    result = dict(kwargs)


    for i in range(1, len(args)+1):

        if i % 4 == 1:
            result["a"] += args[i-1]
        elif i % 4 == 2:
            result["s"] -= args[i-1]
        elif i % 4 == 3 and not args[i -1 ] == 0:
            result["d"] /= args[i-1]
        elif i % 4 == 0:
            result["m"] *= args[i-1]

    return result

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
