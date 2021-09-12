original_text = input()

new_text = ""
new_text += original_text[0]

for i in range(1, len(original_text)):
    if not original_text[i] == original_text[i-1]:
        new_text += original_text[i]
    else:
        continue

print(new_text)