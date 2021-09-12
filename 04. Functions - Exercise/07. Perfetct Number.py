def is_perfect_number(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    if number == sum(divisors):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


given_number = int(input())
is_perfect_number(given_number)