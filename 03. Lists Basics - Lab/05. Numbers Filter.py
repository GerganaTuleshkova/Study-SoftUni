number_of_lines = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(number_of_lines):
    given_num = int(input())
    if given_num % 2 == 0:
        even_list.append(given_num)
    else:
        odd_list.append(given_num)
    if given_num >= 0:
        positive_list.append(given_num)
    else:
        negative_list.append(given_num)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "positive":
    print(positive_list)
else:
    print(negative_list)