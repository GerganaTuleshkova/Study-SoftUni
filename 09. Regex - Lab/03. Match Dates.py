import re

dates = input()

pattern = r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

#matches = re.findall(pattern, dates)
matches_2 = re.finditer(pattern, dates)

# some tests follow below
# print(matches)
# for i in matches:
#     print(i)
# print("....................")

# print(matches_2)
# for j in matches_2:
#     print(j)
# print("....................")

print("Bellow is the result of match_object.groupdict() method\n")
for p in matches_2:
    as_dict = p.groupdict()
    print(as_dict)
print("....................")
print("Bellow is the print for the problem:\n")
# this is the end of the test, comment them
#
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
