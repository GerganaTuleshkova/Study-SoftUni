from collections import deque

effects_queue = deque([int(x) for x in input().split(", ")])
casings_stack = [int(x) for x in input().split(", ")]

cherry_bombs = 0
datura_bombs = 0
smoke_dekoy_bombs = 0
pouch_filled = False

while effects_queue and casings_stack:
    current_effect = effects_queue.popleft()
    current_casing = casings_stack.pop()
    sum = current_casing + current_effect
    if sum == 40:
        datura_bombs += 1
    elif sum == 60:
        cherry_bombs += 1
    elif sum == 120:
        smoke_dekoy_bombs += 1
    else:
        effects_queue.insert(0, current_effect)
        casings_stack.append(current_casing - 5)
    if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_dekoy_bombs >= 3:
        pouch_filled = True
        break

if pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not effects_queue:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects_queue])}")

if not casings_stack:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings_stack])}")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_dekoy_bombs}")
