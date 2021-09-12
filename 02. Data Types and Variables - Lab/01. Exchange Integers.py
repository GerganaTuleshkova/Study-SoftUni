a = int(input())
b = int(input())

print(f"Before:\na = {a}\nb = {b}")
a_old = a
a = b
b = a_old
print(f"After:\na = {a}\nb = {b}")