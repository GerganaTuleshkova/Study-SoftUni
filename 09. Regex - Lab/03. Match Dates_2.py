import re

dates = input()

pattern = r"\b(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})\b"

valid_dates = re.finditer(pattern, dates)

for date in valid_dates:
    as_dict = date.groupdict()
    print(f"Day: {as_dict['day']}, Month: {as_dict['month']}, Year: {as_dict['year']}")

