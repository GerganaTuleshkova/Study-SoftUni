text = input()

characters = {}

for ch in text:
    if ch == " ":
        continue
    if ch not in characters:
        characters[ch] = 0
    characters[ch] += 1

for letter, occurances in characters.items():
    print(f"{letter} -> {occurances}")
