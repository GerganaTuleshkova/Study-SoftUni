def is_main_color(sub1, sub2):
    if sub1 + sub2 in main_colors:
        return sub1 + sub2
    elif sub2 + sub1 in main_colors:
        return sub2 + sub1
    return False

def is_secondary_color(sub1, sub2):
    if sub1 + sub2 in secondary_colors:
        return sub1 + sub2
    elif sub2 + sub1 in secondary_colors:
        return sub2 + sub1
    return False


def is_color(sub1, sub2):
    if sub1 + sub2 in secondary_colors or sub1 + sub2 in main_colors:
        return sub1 + sub2
    elif sub2 + sub1 in secondary_colors or sub2 + sub1 in main_colors:
        return sub2 + sub1
    return False



substrings = input().split()
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
secondary_colors_needs = {
    "orange" : ["red", "yellow"],
    "purple" : ["red", "blue"],
    "green" : ["blue", "yellow"] }

colors_found = []

while substrings:
    if len(substrings) > 1:
        if is_color(substrings[0], substrings[-1]):
            colors_found.append(is_color(substrings[0], substrings[-1]))
            substrings = substrings[1:-1]
        else:
            sub_1 = substrings[0][:-1]
            sub_2 = substrings[-1][:-1]
            substrings = substrings[1:-1]
            index_to_insert = (len(substrings)) // 2
            if sub_2:
                substrings.insert(index_to_insert, sub_2)
            if sub_1:
                substrings.insert(index_to_insert, sub_1)
    else:
        if is_color(substrings[0], ""):
            colors_found.append(substrings[0])
            substrings.pop()
        else:
            substrings[0] = substrings[0][:-1]
            if not substrings[0]:
                substrings.pop()

for color in colors_found:
    if color in secondary_colors_needs:
        needs_found = True
        for prime_color in secondary_colors_needs[color]:
            if prime_color not in colors_found:
                needs_found = False
        if not needs_found:
            colors_found.remove(color)


print(colors_found)






