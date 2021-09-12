sequence = [int(n) for n in input().split()]

average_num = sum(sequence)/ len(sequence)

above_average = [n for n in sequence if n > average_num]
above_average.sort(reverse=True)

if len(above_average) > 5:
    for i in range(5):
        print(above_average[i], end=" ")
elif 0 < len(above_average) <=5:
    print(" ".join([str(n) for n in above_average]))
elif len(above_average) == 0:
    print("No")