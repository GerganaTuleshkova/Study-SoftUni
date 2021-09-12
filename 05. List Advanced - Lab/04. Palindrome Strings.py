given_words = input().split()
key_palindrome = input()

palindromes = []

for word in given_words:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(key_palindrome)} times")