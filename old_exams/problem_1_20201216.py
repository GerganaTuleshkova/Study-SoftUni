from collections import deque


males_stack = [int(n) for n in input().split()]
females_queue = deque([int(n) for n in input().split()])
matches = 0

while males_stack and females_queue:
    male = males_stack[-1]
    female = females_queue[0]

    if male <= 0:
        males_stack.pop()
        continue
    if female <= 0:
        females_queue.popleft()
        continue

    if male % 25 == 0:
        males_stack.pop()
        males_stack.pop()
        continue

    if female % 25 == 0:
        females_queue.popleft()
        females_queue.popleft()
        continue

    if female == male:
        males_stack.pop()
        females_queue.popleft()
        matches += 1
    else:
        females_queue.popleft()
        males_stack[-1] -= 2


print(f"Matches: {matches}")
if not males_stack:
    print("Males left: none")
else:
    print(f"Males left: {', '.join([str(x) for x in males_stack[::-1]])}")

if not females_queue:
    print("Females left: none")
else:
    print(f"Females left: {', '.join([str(x) for x in females_queue])}")
