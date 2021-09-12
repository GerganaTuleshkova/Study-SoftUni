people_waiting = int(input())
lift = [int(n) for n in input().split()]


for num in range(len(lift)):
    if people_waiting >= 4 - lift[num]:
        people_waiting -= (4 - lift[num])
        lift[num] = 4
    else:
        lift[num] += people_waiting
        people_waiting = 0
        break
    if people_waiting == 0:
        break

if people_waiting == 0 and (sum(lift) / len(lift) < 4):
    print("The lift has empty spots!")

elif people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")

print(" ".join([str(i) for i in lift]))