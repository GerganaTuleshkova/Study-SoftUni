def find_type_coordinates(text):
    type = ""
    coordinates = ""
    i = 0
    while i < len(text):
        if text[i] == "&":
            next_ch = text[i + 1]
            j = i
            while not next_ch == "&" and not i == len(text):
                type += next_ch
                j += 1
                if j < len(text)-1:
                    next_ch = text[j + 1]
                else:
                    break
            i += len(type) +1
        if text[i] == "<":
            next_ch = (text[i + 1])
            k = i
            while not next_ch == ">" and not i == len(text):
                coordinates += next_ch
                k += 1
                if k < len(text)-1:
                    next_ch = (text[k + 1])
                else:
                    break
            i += len(coordinates) + 1
        i += 1
    return type, coordinates


keys = [int(n) for n in input().split()]

text = input()
hidden_message = ""
key_at_index = 0
while not text == "find":

    for ch in text:
        hidden_ch = chr(ord(ch) - keys[key_at_index])
        hidden_message += hidden_ch
        key_at_index += 1
        if key_at_index == len(keys):
            key_at_index = 0
    found_type, found_coordinate = find_type_coordinates(hidden_message)

    print(f"Found {found_type} at {found_coordinate}")
    hidden_message = ""
    key_at_index = 0

    text = input()