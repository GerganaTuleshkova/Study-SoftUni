from collections import deque

bullet_price = int(input())
barrel_capacity = int(input())
bullets_stack = [int(n) for n in input().split()]
locks = deque([int(n) for n in input().split()])
prize = int(input())

bullets_costs = 0
fired_bullets_count = 0

while locks and bullets_stack:

    current_bullet = bullets_stack[-1]
    lock_to_shoot = locks[0]

    if current_bullet <= lock_to_shoot:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    bullets_stack.pop()
    fired_bullets_count += 1

    if fired_bullets_count % barrel_capacity == 0 and bullets_stack:
        print("Reloading!")

money_earned = prize - (fired_bullets_count * bullet_price)

if not locks:
    print(f"{len(bullets_stack)} bullets left. Earned ${money_earned}")
elif not bullets_stack:
    print(f"Couldn't get through. Locks left: {len(locks)}")