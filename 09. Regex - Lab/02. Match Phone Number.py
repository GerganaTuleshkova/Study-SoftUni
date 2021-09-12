import re

numbers = input()

pattern = r"\+359( |-)2\1[0-9]{3}\1[0-9]{4}\b"

matches = re.finditer(pattern, numbers)


valid_phones = [match.group() for match in matches]
print(", ".join(valid_phones))
