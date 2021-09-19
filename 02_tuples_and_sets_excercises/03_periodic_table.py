lines_of_input = int(input())

ch_elements = set()

for _ in range(lines_of_input):
    elements = input().split()
    for el in elements:
        ch_elements.add(el)
    # second option
    # [ch_elements.add(el) for el in input().split()]

    # third option
    # elements = set(input().split())
    # ch_elements = ch_elements.union(elements)

[print(el) for el in ch_elements]


