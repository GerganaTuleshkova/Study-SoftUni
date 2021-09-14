given_string = input()

parentheses_indecis_stack = []

for i in range(len(given_string)):
    if given_string[i] == "(":
        parentheses_indecis_stack.append(i)
    elif given_string[i] == ")":
        start_of_substring = parentheses_indecis_stack.pop()
        end_of_string = i
        print(given_string[start_of_substring:end_of_string+1])
