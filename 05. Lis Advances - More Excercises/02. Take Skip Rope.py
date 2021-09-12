characters_list = [x for x in input()]

letters_list = [x for x in characters_list if not x.isdigit()]
digits_list = [int(x) for x in characters_list if x.isdigit()]

take_digits = [digits_list[i] for i in range(len(digits_list)) if i % 2 == 0]
leave_digits = [digits_list[i] for i in range(len(digits_list)) if i % 2 != 0]

final_result = []

for i in range(len(take_digits)):
    take_n = take_digits[i]
    skip_n = leave_digits[i]
    for num in range(take_n):
        if num+1 > len(letters_list):
            break
        final_result.append(letters_list[num])
    for _ in range(take_n + skip_n):
        if not letters_list:
            break
        letters_list.pop(0)



print("".join(final_result))

