import re

text = input()
pattern = r"(?<=\s_)[a-zA-Z0-9]+\b|(?<=^_)[a-zA-Z0-9]+\b"
#or
#pattern = r"\b_[a-zA-Z0-9]+\b"

names = re.findall(pattern, text)
print(",".join(names))