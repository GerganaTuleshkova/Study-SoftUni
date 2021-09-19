def check_if_any_subset(set1, set2):
    return set1.issubset(set2) or set2.issubset(set1)


set_1 = set([int(n) for n in input().split()])
set_2 = set([int(n) for n in input().split()])

n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    set_to_manipulate = command[1]
    if set_to_manipulate == "First":
        set_to_manipulate = set_1
    elif set_to_manipulate == "Second":
        set_to_manipulate = set_2
    if action == "Add":
        for n in command[2:]:
            set_to_manipulate.add(int(n))
    elif action == "Remove":
        for n in command[2:]:
            if int(n) in set_to_manipulate:
                set_to_manipulate.remove(int(n))
    elif action == "Check":
        print(check_if_any_subset(set_1, set_2))

print(", ".join(str(n) for n in sorted(set_1)))
print(", ".join(str(n) for n in sorted(set_2)))


