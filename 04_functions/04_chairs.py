def combinations(names, count, selected_names=[]):

    if len(selected_names) == count:
        print(", ".join(selected_names))
        return

    for i in range(len(names)):
        selected_names.append(names[i])
        combinations(names[i+1:], count, selected_names)
        selected_names.pop()


names = input().split(", ")
count = int(input())
combinations(names, count)