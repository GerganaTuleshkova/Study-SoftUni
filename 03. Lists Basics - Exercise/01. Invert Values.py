given_string = input()

string_as_list = given_string.split(" ")
opposities_list = []
for el in string_as_list:
    opposities_list.append(-1*int(el))
print(opposities_list)