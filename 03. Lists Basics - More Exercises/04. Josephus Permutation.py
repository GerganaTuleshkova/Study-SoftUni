soldiers_list = input().split()
key = int(input())

killed_soldiers = []
start = key
while len(soldiers_list) > 0:
    index_to_kill = 0

    if key > len(soldiers_list):
        index_to_kill = key % len(soldiers_list)
        killed_soldiers.append(soldiers_list.pop(index_to_kill - 1))
    else:
        index_to_kill = key

        soldiers_to_kill = soldiers_list[start-1::index_to_kill]
        start -= len(soldiers_list) % key
        for soldier in soldiers_to_kill:
            killed_soldiers.append(soldier)
        for soldier in soldiers_to_kill:
            soldiers_list.remove(soldier)

killed_soldiers_int = [int(x) for x in killed_soldiers]
print("[",end="")
print(",".join(killed_soldiers), end="")
print("]")