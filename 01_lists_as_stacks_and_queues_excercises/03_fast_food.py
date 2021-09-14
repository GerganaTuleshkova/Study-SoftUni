from collections import deque

food_qty = int(input())
orders_queue = deque([int(n) for n in input().split()])

print(max(orders_queue))

while orders_queue:
    current_order = orders_queue[0]
    if food_qty >= current_order:
        food_qty -= orders_queue.popleft()
    else:
        break

if not orders_queue:
    print("Orders complete")
else:
    print("Orders left: ", end="")
    while orders_queue:
        print(orders_queue.popleft(), end=" ")

