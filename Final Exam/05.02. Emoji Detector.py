import re

text = input()

emojis_list = []
emoji_coolness_dict = {}
treshold = 1
pattern_emoji = r"(?P<separator>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=separator)"
#pattern_emoji = r"(?<![\:|\*])(?P<separator>[\:\:|\*\*])(?P<emoji>[A-Z][a-z]{2,})(?P=separator)(?![\:|\*])"
pattern_digit = r"\d"

digits_as_str = re.findall(pattern_digit, text)
digits = [int(n) for n in digits_as_str]
for digit in digits:
    treshold *= digit

emojis_iter = re.finditer(pattern_emoji, text)

for emoji_iter in emojis_iter:
    emoji_text = emoji_iter.group("emoji")
    separator = emoji_iter.group("separator")
    emoji = separator+emoji_text+separator
    coolness = 0
    for letter in emoji_text:
        coolness += ord(letter)
    emoji_coolness_dict[emoji] = coolness


    emojis_list.append(emoji)

print(f"Cool threshold: {treshold}")
print(f"{len(emoji_coolness_dict)} emojis found in the text. The cool ones are:")
for k, v in emoji_coolness_dict.items():
    if v >= treshold:
        print(k)