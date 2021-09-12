def command_execution(command, given_list):
    odd_elements = []
    even_elements = []
    for el in given_list:
        if el % 2 != 0:
            odd_elements.append(el)
        elif el % 2 == 0:
            even_elements.append(el)
    if "exchange" in command:
        execution_command = command.split()
        index_to_cut = int(execution_command[1]) # takes the second element of the
        # list which should be the index to split and turns it into integer
        if index_to_cut + 1 > len(given_list):
            print("Invalid index")
        else:
            half_1_list = given_list[:index_to_cut + 1]
            half_2_list = given_list[index_to_cut + 1:]
            new_list = half_2_list + half_1_list
            given_list = new_list
            return given_list
    elif "max" in command or "min" in command:

        if "odd" in command:
            if len(odd_elements) == 0: # there are no odd numbers int he list
                print("No matches")
            else:
                if "max" in command:
                    return given_list.index(max(odd_elements))
                else:
                    return given_list.index(min(odd_elements))
        elif "even" in command:
            if len(even_elements) == 0: # there are no even numbers int he list
                print("No matches")
            else:
                if "max" in command:
                    return given_list.index(max(even_elements))
                else:
                    return given_list.index(min(even_elements))
    elif "first" in command or "last" in command:
        execution_command = command.split()
        index_to_count = int(execution_command[1])  # takes the second element
        if "odd" in command:
            if index_to_count > len(odd_elements):
                print("Invalid count")
            else:
                if "first" in command:
                    odd_el_extract = odd_elements[:index_to_count]
                    print(odd_el_extract)
                elif "last" in command:
                    odd_el_extract = odd_elements[-1:index_to_count, -1]
                    print(odd_el_extract)
        elif "even" in command:
            if index_to_count > len(even_elements):
                print("Invalid count")
            else:
                if "first" in command:
                    even_el_extract = even_elements[:index_to_count]
                    print(even_el_extract)
                elif "last" in command:
                    even_el_extract = even_elements[-1:index_to_count, -1]
                    print(even_el_extract)


list_of_numbers_as_string = input().split()
given_list = []
for i in list_of_numbers_as_string:
    given_list.append(int(i))

odd_elements = []
even_elements = []
for el in given_list:
    if el % 2 != 0:
        odd_elements.append(el)
    elif el % 2 == 0:
        even_elements.append(el)

command = input()
while not command == "end":
    # odd_elements = []
    # even_elements = []
    # for el in given_list:
    #     if el % 2 != 0:
    #         odd_elements.append(el)
    #     elif el % 2 == 0:
    #         even_elements.append(el)
    if "exchange" in command:
        execution_command = command.split()
        index_to_cut = int(execution_command[1])  # takes the second element of the
        # list which should be the index to split and turns it into integer
        if index_to_cut + 1 > len(given_list) or index_to_cut < 0:
            print("Invalid index")
        else:
            half_1_list = given_list[:index_to_cut + 1]
            half_2_list = given_list[index_to_cut + 1:]
            new_list = half_2_list + half_1_list
            given_list = new_list

    elif "max" in command or "min" in command:
        reversed_list = given_list[::-1]
        if "odd" in command:
            if len(odd_elements) == 0:  # there are no odd numbers int he list
                print("No matches")
            else:

                if "max" in command:

                    print(reversed_list.index(max(odd_elements)))
                else:
                    print(reversed_list.index(min(odd_elements)))
        elif "even" in command:
            if len(even_elements) == 0:  # there are no even numbers int he list
                print("No matches")
            else:
                if "max" in command:
                    print(reversed_list.index(max(even_elements)))
                else:
                    print(reversed_list.index(min(even_elements)))
    elif "first" in command or "last" in command:
        execution_command = command.split()
        index_to_count = int(execution_command[1])  # takes the second element
        if "odd" in command:
            if index_to_count > len(given_list):
                print("Invalid count")
            elif index_to_count >= len(odd_elements):
                print(odd_elements)
            else:
                if "first" in command:
                    odd_el_extract = odd_elements[:index_to_count]
                    print(odd_el_extract)
                elif "last" in command:
                    odd_el_extract = odd_elements[-1:index_to_count, -1]
                    print(odd_el_extract)
        elif "even" in command:
            if index_to_count > len(given_list):
                print("Invalid count")
            elif index_to_count >= len(even_elements):
                print(even_elements)
            else:
                if "first" in command:
                    even_el_extract = even_elements[:index_to_count]
                    print(even_el_extract)
                elif "last" in command:
                    even_el_extract = even_elements[-1:index_to_count, -1]
                    print(even_el_extract)
    command = input()
print(given_list)