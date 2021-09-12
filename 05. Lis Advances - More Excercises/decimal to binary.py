decimal_number = int(input())
binary_as_list = []


while decimal_number > 0:
    result = decimal_number // 2
    remainder = decimal_number % 2
    binary_as_list.append(remainder)

    decimal_number = result

print("".join(reversed([str(i) for i in binary_as_list])))


print(binary_as_list)