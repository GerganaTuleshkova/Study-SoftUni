numbers_string = input()
n = int(input())

num_list = numbers_string.split(" ")
numbers_list = []
for i in num_list:
    numbers_list.append(int(i))
sorted_list = sorted(numbers_list)
#sorted_list.sort()

# biggest_list = sorted_list[n:]
# new_list.sort(reverse=True)
# for number in new_list:
#     print(number, end=", ")

drop_outs = sorted_list[0:n]
for drop in drop_outs:
    numbers_list.remove(drop)


for i in range(len(numbers_list)-1):
    print(numbers_list[i],end=", ")
print(numbers_list[-1])