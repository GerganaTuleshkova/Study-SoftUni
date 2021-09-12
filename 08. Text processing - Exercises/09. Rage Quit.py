given_string = input()
unique_letters = []
repeat = 0
string_to_print = ""
final_string = ""

for i in range(0, len(given_string)):
    if not given_string[i].isdigit():
        string_to_print += given_string[i]
        unique_letters.append(given_string[i].lower())
    else:
        if i < len(given_string)-1:
            if given_string[i+1].isdigit():
                repeat = int(given_string[i])*10 + int(given_string[i+1])
            else:
                repeat = int(given_string[i])
        else:
            repeat = int(given_string[i])

        final_string += string_to_print.upper() * repeat
        string_to_print = ""

print(f"Unique symbols used: {len(set(unique_letters))}")
print(final_string)
