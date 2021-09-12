def sum_numbers(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2, num_3):
    sum = sum_numbers(num_1, num_2)
    return (sum - num_3)

def add_and_subtract(num_1, num_2, num_3):
    return subtract(num_1, num_2, num_3)

n_1 = int(input())
n_2 = int(input())
n_3 = int(input())


print(add_and_subtract(n_1, n_2, n_3))
