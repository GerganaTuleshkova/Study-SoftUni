n = int(input())
longest_intersection_length = 0
longest_intersection = set()
for _ in range(n):
    set_1 = set()
    set_2 = set()
    info = input().split("-")
    set_1_info = info[0]
    set_2_info = info[1]

    start_1, end_1 = set_1_info.split(",")
    start_1 = int(start_1)
    end_1 = int(end_1)
    for i in range(start_1, end_1 +1):
        set_1.add(i)

    start_2, end_2 = set_2_info.split(",")
    start_2 = int(start_2)
    end_2 = int(end_2)
    for i in range(start_2, end_2 + 1):
        set_2.add(i)

    intersection = set_1.intersection(set_2)

    if len(intersection) > longest_intersection_length:
        longest_intersection_length = len(intersection)
        longest_intersection = intersection

l_intersection_numbers = ", ".join([str(n) for n in longest_intersection])
print(f"Longest intersection is [{l_intersection_numbers}] with length {longest_intersection_length}")