number = int(input())
litters_poured = 0

for tern in range(1, number + 1):
    litters = int(input())
    if (255 - litters_poured) < litters:
        print("Insufficient capacity!")
        continue
    else:
        litters_poured += litters

print(litters_poured)