given_string = input()
beggars_count = int(input())
bringings = given_string.split(", ")
all_sums_list = []


for beggar in range(beggars_count):
    temp = bringings[beggar::beggars_count]
    for j in range(len(temp)):
        temp[j] = int(temp[j])
    all_sums_list.append(sum(temp))

print(all_sums_list)

