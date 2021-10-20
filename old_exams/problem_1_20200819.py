from collections import deque

customers_queue = deque([int(x) for x in input().split(", ")])
taxis_stack = [int(x) for x in input().split(", ")]

total_time = 0

while customers_queue and taxis_stack:
    current_customer = customers_queue[0]
    current_taxi = taxis_stack[-1]

    if current_taxi >= current_customer:
        total_time += current_customer
        customers_queue.popleft()
        taxis_stack.pop()

    else:
        taxis_stack.pop()

if not customers_queue:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers_queue])}")