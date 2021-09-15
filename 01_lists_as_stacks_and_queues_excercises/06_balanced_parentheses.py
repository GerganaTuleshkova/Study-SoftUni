given_string = input()

opening_parentheses = []

is_balanced = True

for ch in given_string:
    if ch in ["(", "[", "{"]:
        opening_parentheses.append(ch)
    elif ch in [")", "]", "}"] and opening_parentheses:
        if ch == ")" and opening_parentheses.pop() == "(" \
                or ch == "]" and opening_parentheses.pop() == "[" \
                or ch == "}" and opening_parentheses.pop() == "{":
            pass
        else:
            is_balanced = False
            break
    else:
        is_balanced = False

print("YES" if is_balanced else "NO")

