from collections import deque

fireworks_effect_queue = deque([int(n) for n in input().split(", ")])
explosive_power_stack = [int(n) for n in input().split(", ")]

palm_count = 0
willow_count = 0
crossette_count = 0

while fireworks_effect_queue and explosive_power_stack:
    if fireworks_effect_queue[0] <= 0:
        fireworks_effect_queue.popleft()
        continue
    if explosive_power_stack[-1] <= 0:
        explosive_power_stack.pop()
        continue
    current_sum = fireworks_effect_queue[0] + explosive_power_stack[-1]
    if current_sum % 3 == 0 and not current_sum % 5 == 0:
        palm_count += 1
        fireworks_effect_queue.popleft()
        explosive_power_stack.pop()
    elif current_sum % 5 == 0 and not current_sum % 3 == 0:
        willow_count += 1
        fireworks_effect_queue.popleft()
        explosive_power_stack.pop()
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette_count += 1
        fireworks_effect_queue.popleft()
        explosive_power_stack.pop()
    else:
        fireworks_effect_queue[0] -= 1
        fireworks_effect_queue.append(fireworks_effect_queue[0])
        fireworks_effect_queue.popleft()

    if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
        break

if palm_count >= 3 and willow_count >= 3 and crossette_count >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect_queue:
    print("Firework Effects left: ", end="")
    print(", ".join([str(n) for n in fireworks_effect_queue]))

if explosive_power_stack:
    print("Explosive Power left: ", end="")
    print((", ".join([str(n) for n in explosive_power_stack])))


print(f"Palm Fireworks: {palm_count}")
print(f"Willow Fireworks: {willow_count}")
print(f"Crossette Fireworks: {crossette_count}")