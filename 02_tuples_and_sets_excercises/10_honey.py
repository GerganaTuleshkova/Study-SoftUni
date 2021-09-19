from collections import deque


def make_calculation(num_1, num_2, operator):
    if operator == "*":
        return abs(num_1 * num_2)
    elif operator == "+":
        return abs(num_1 + num_2)
    elif operator == "-":
        return abs(num_1 - num_2)
    elif operator == "/":
        return abs(num_1 / num_2)


honey_made = 0
bee_queue = deque([int(n) for n in input().split()])
nectar_stack = [int(n) for n in input().split()]
symbols_queue = deque([n for n in input().split()])

while bee_queue and nectar_stack:
    current_bee = bee_queue[0]
    current_nectar = nectar_stack[-1]
    if current_nectar >= current_bee:
        operator = symbols_queue[0]
        current_honey = make_calculation(current_bee, current_nectar, operator)
        honey_made += current_honey
        bee_queue.popleft()
        nectar_stack.pop()
        symbols_queue.popleft()

    else:
        nectar_stack.pop()


print(f"Total honey made: {honey_made}")

if bee_queue:
    print(f"Bees left: {', '.join([str(n) for n in bee_queue])}")
if nectar_stack:
    print(f"Nectar left: {', '.join([str(n) for n in nectar_stack])}")