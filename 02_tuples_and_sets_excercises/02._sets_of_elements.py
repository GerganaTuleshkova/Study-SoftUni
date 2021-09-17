n, m = input().split()
n = int(n)
m = int(m)

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

intersection = set_n.intersection(set_m)

[print(n) for n in intersection]