def product_kind(n1, n2, n3):
    all_numbers = [n1, n2, n3]
    positive_numbers = []
    negative_numbers = []
    zeroes = []
    for n in all_numbers:
        if n == 0:
            zeroes.append(n)
        elif n > 0:
            positive_numbers.append(n)
        else:
            negative_numbers.append(n)

    if len(zeroes) > 0:
        print("zero")
    elif len(negative_numbers) % 2 == 0:
        print("positive")
    else:
        print("negative")


n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
product_kind(n_1, n_2, n_3)