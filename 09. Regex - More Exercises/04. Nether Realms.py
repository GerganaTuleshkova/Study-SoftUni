import re

text = input()

pattern_split = r"\,\s*"
demons_info = sorted(re.split(pattern_split, text))

patter_for_sum = r"[^-0-9+/*///.]"
pattern_base_damage = r"[\+|\-]?\d+\.?\d*"
pattern_multipliers = r"[\/|\*]"
pattern_demon_name = r"[^\s\,]+"
for info in demons_info:
    demon = re.match(pattern_demon_name, info).group()
    if " " in demon:
        continue
    health = 0
    chars_to_sum = re.findall(patter_for_sum, demon)
    for char in chars_to_sum:
        health += ord(char)
    base_damage = 0
    numbers_to_sum = re.finditer(pattern_base_damage, demon)
    for num in numbers_to_sum:
        base_damage += float(num.group())
    multipliers = re.findall(pattern_multipliers, demon)

    for multiplier in multipliers:
        if multiplier == "*":
            base_damage *= 2
        elif multiplier == "/":
            base_damage /= 2
    print(f"{demon} - {health} health, {base_damage:.2f} damage")


