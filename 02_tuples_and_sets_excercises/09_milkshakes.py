from collections import deque

chocolate_stack = [int(n) for n in input().split(", ")]
milk_queue = deque([int(n) for n in input().split(", ")])

milkshakes_count = 0

while milkshakes_count < 5 and chocolate_stack and milk_queue:
    current_chocolate = chocolate_stack[-1]
    current_milk = milk_queue[0]
    
    if current_chocolate <= 0 or current_milk <= 0:
        if current_chocolate <= 0:
            chocolate_stack.pop()
        if current_milk <= 0:
            milk_queue.popleft()
        continue

    if current_milk == current_chocolate:
        milkshakes_count += 1
        chocolate_stack.pop()
        milk_queue.popleft()
    else:
        milk_to_move = milk_queue.popleft()
        milk_queue.append(milk_to_move)
        chocolate_stack[-1] -= 5

if milkshakes_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print(f"Chocolate: {', '.join([str(n) for n in chocolate_stack])}")
else:
    print("Chocolate: empty")

if milk_queue:
    print(f"Milk: {', '.join([str(n) for n in milk_queue])}")
else:
    print("Milk: empty")