def factorial_division(num_1, num_2):
    factorial_1 = 1
    for n in range(2, num_1+1):
        factorial_1 *= n
    factorial_2 = 1
    for n in range(2, num_2+1):
        factorial_2 *= n
    result = factorial_1 / factorial_2
    print(f"{result:.2f}")


number_1 = int(input())
number_2 = int(input())

factorial_division(number_1, number_2)
