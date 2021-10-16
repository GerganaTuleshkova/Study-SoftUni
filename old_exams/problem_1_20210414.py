from collections import deque


orders_queue = deque([int(x) for x in input().split(", ") if 0 < int(x) <= 10])
capacities_stack = [int(x) for x in input().split(", ")]

pizzas_made = 0

while orders_queue and capacities_stack:
    current_order = orders_queue[0]
    current_capacity = capacities_stack[-1]
    if current_capacity >= current_order:
        pizzas_made += current_order
        orders_queue.popleft()
        capacities_stack.pop()
    else:
        orders_queue[0] -= current_capacity
        pizzas_made += current_capacity
        capacities_stack.pop()

if not orders_queue:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {pizzas_made}")
    print(f"Employees: {', '.join([str(x) for x in capacities_stack])}")
elif orders_queue and not capacities_stack:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders_queue])}")
