soldiers_list = input().split()
key = int(input())

killed_soldiers = []
counter = 0
index_to_kill = 0

while len(soldiers_list) > 0:
    counter += 1
    if counter % key == 0:
        killed_soldiers.append(soldiers_list.pop(index_to_kill))
    else:
        index_to_kill += 1
    if index_to_kill >= len(soldiers_list):
        index_to_kill = 0


killed_soldiers_int = [int(x) for x in killed_soldiers]
print("[",end="")
print(",".join(killed_soldiers), end="")
print("]")

# print(killed_soldiers)