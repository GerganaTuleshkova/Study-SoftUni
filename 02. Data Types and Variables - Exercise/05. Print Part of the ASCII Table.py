start_sequence = int(input())
end_sequence = int(input())

for num in range(start_sequence, end_sequence +1):
    print(f"{chr(num)} ",end="")