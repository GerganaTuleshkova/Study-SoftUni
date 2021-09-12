def tribunacci_sequense_by_count(count):
    tribunacci_sequence = []
    for i in range(count):
        if i == 0:
            n = 1

        elif i == 1:
            n = tribunacci_sequence[i-1]

        elif i == 2:
            n = n + tribunacci_sequence[i-2]
        elif i > 2:
            n = n + tribunacci_sequence[i-2] + tribunacci_sequence[i-3]
        tribunacci_sequence.append(n)
    return tribunacci_sequence

count = int(input())
sequence = tribunacci_sequense_by_count(count)

for n in sequence:
    print(n, end=" ")

