from collections import deque

cups_queue = deque([int(n) for n in input().split()])
bottles_stack =[int(n) for n in input().split()]

wasted_water = 0

while cups_queue and bottles_stack:
    current_cup = cups_queue[0]
    current_bottle = bottles_stack.pop()
    if current_cup <= current_bottle:
        wasted_water += current_bottle - cups_queue.popleft()
    else:
        cups_queue[0] -= current_bottle


if not cups_queue:
    print(f"Bottles: ", end="")
    while bottles_stack:
        print(f"{bottles_stack.pop()}", end=" ")
    print()

else:
    print("Cups: ", end="")
    while cups_queue:
        print(f"{cups_queue.popleft()}", end=" ")
    print()

print(f"Wasted litters of water: {wasted_water}")
