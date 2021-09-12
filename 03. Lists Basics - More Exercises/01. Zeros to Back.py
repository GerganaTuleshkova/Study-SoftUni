nums_as_string_list = input().split(", ")
integers_list = [int(x) for x in nums_as_string_list]

zeros_list = []
non_zero_list = []
for number in integers_list:
    if number == 0:
        zeros_list.append(number)
    else:
        non_zero_list.append(number)

print(non_zero_list+zeros_list)
