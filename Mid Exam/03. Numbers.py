sequence = [int(n) for n in input().split()]

sequence.sort(reverse=True)
average_num = sum(sequence) / len(sequence)
top_5_higher_than_average = []


for el in sequence:
    if el > average_num:
        top_5_higher_than_average.append(el)

if len(top_5_higher_than_average) > 5:
    for i in range(5):
        print(top_5_higher_than_average[i], end=" ")
elif len(top_5_higher_than_average) > 0:
    print(" ".join([str(n) for n in top_5_higher_than_average]))
else:
    print("No")