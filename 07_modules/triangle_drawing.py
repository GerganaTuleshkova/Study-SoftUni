def draw_triangle(n):

    line = []
    for i in range(1, n + 1):
        line.append(i)
        print(" ".join(str(x) for x in line))
    for i in range(n - 1):
        line.pop()
        print(" ".join(str(x) for x in line))



