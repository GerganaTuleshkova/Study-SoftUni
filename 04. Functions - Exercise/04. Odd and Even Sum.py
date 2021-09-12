def sum_of_odd_and_even(number):
    sum_odd = 0
    sum_even = 0

    for digit_as_letter in str(number):
        if int(digit_as_letter) % 2 == 0:
            sum_even += int(digit_as_letter)
        else:
            sum_odd += int(digit_as_letter)

    return sum_odd, sum_even


number_given = int(input())
odd_sum, even_sum = sum_of_odd_and_even(number_given)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
