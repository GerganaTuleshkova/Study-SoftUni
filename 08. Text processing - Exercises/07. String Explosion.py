original_text = input()

new_text = original_text[:]
derived_text = ""
strength = 0

i = 0
while i < len(new_text):
    if new_text[i] == ">":
        current_explosion = int(new_text[i+1])
        strength += current_explosion
    else:
        if strength > 0:
            new_text = new_text[:i] + new_text[i+1:]
            i -= 1
            strength -= 1

    i +=1

print(new_text)
