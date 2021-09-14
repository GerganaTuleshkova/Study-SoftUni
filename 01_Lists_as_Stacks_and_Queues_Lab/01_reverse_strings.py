given_string = input()

stack = []

for ch in given_string:
    stack.append(ch)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print(reversed_string)