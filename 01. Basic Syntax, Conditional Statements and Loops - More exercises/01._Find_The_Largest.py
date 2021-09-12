# number = int(input())
# number_as_list = []
#
# number_as_string = str(number)
# for digit in number_as_string:
#     number_as_list.append(int(digit))
# number_as_list.sort(reverse=True)
# for digit in number_as_list:
#     print(digit, end="")

number = list(input())

number.sort(reverse=True)
for digit in number:
    print(digit, end="")