given_text = input()

letters_used = set()

for ch in given_text:
    letters_used.add(ch)

for ch in sorted(letters_used):
    print(f"{ch}: {given_text.count(ch)} time/s")


