import re
text = input()

searched_word = input()
pattern = searched_word+r"\b"

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))