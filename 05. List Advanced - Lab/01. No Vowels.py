letters = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

no_vowels_list = [x for x in letters if x not in vowels]
print("".join(no_vowels_list))

# no_vowels_list = "".join([x for x in letters if x not in vowels])
# print(no_vowels_list)