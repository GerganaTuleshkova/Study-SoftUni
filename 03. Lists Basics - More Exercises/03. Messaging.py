sequence_of_numbers = input().split()
string_with_chars = input()

string_as_list = [char for char in string_with_chars]
#print(string_as_list)

message = []
for number_as_str in sequence_of_numbers:
    sum_of_digits = 0
    for i in range(len(number_as_str)):
        sum_of_digits += int(number_as_str[i])
    #print(sum_of_digits)
    if sum_of_digits > len(string_as_list):
        index = sum_of_digits % len(string_as_list)
    else:
        index = sum_of_digits
    message.append(string_as_list[index])
    string_as_list.pop(index)
    #print(string_as_list)
print("".join(message))
