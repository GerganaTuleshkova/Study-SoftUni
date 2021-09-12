def is_shot(item):
    if item == -1:
        return True


targets = [int(n) for n in input().split()]

command = input()

while not command == "End":
    index = int(command)
    if 0 <= index < len(targets):
        if not is_shot(targets[index]):
            # for target in targets:
            #     if target <= targets[index] and not is_shot(target):
            #         target = targets[index]
            #     elif target > targets[index] and not is_shot(target) :
            #         target -= targets[index]
            value = targets[index]
            for i in range(0, len(targets)):
                if targets[i] <= value and not is_shot(targets[i]):
                    targets[i] += value
                elif targets[i] > value and not is_shot(targets[i]):
                    targets[i] -= value
            targets[index] = -1

    command = input()

shot_targets = [t for t in targets if is_shot(t)]
result = f"Shot targets: {len(shot_targets)} -> "
result += " ".join([str(t) for t in targets])
print(result)