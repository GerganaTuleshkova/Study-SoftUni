
lines = int(input())
brakets_list = []
for line in range(1, lines + 1):
    given_string = input()
    if given_string == "(" or given_string == ")":
        brakets_list.append(given_string)

is_balanced = True
if brakets_list[0] == ")":
    is_balanced = False
else:
    for index, element in enumerate(brakets_list):
        if index != 0 and index % 2 == 0:
            if not element == "(":
                is_balanced = False
                break
        elif index != 0 and not index % 2 == 0:
            if not element == ")":
                is_balanced = False
                break
if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")