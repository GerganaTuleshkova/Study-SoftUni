given_numbers = [int(n) for n in input().split(", ")]
# max_item = max(given_numbers)
#
# max_group = max_item // 10
#
# if max_group >= 0:
#     print("Group of 10's: "+f"{[num for num in given_numbers if num // 10 < 1]}")
# if max_group >= 1:
#     print("Group of 20's: "+f"{[num for num in given_numbers if (num // 10 < 2) and (num // 10 >= 1)]}")
# if max_group >= 2:
#     print("Group of 30's: "+f"{[num for num in given_numbers if (num // 10 < 3) and (num // 10 >= 2)]}")
# if max_group >= 3:
#     print("Group of 40's: "+f"{[num for num in given_numbers if (num // 10 < 4) and (num // 10 >= 3)]}")
# if max_group >= 4:
#     print("Group of 50's: "+f"{[num for num in given_numbers if (num // 10 <= 5) and (num // 10 >= 4)]}")

for boundary in range(1, max(given_numbers) // 10 + 2):
    group_list = [n for n in given_numbers if n <= 10 * boundary]
    max_num = max(given_numbers)
    if max(given_numbers) > 10 * (boundary - 1):
        print(f"Group of {boundary*10}'s: "+f"{group_list}")
    for number in group_list:
        given_numbers.remove(number)
    if len(given_numbers) == 0:
        break
