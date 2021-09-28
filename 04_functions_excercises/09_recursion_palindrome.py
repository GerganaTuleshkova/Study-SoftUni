# def palindrome(word, index):
#     is_palindrome = True
#     if len(word) <= 1:
#         return True
#
#     if word[0] == word[-1] and palindrome(word[1:-1], 0):
#         is_palindrome = True
#     else:
#         is_palindrome = False
#
#     if is_palindrome:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"
#


def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("hanah", 0))
print(palindrome("hjgf'wejfkl", 0))
