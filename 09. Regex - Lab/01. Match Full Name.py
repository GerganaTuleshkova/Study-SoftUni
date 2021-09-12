import re

#Trying some changes now

names = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(pattern, names)

print(" ".join(matches))