from collections import deque

people = deque([name for name in input().split()])

step = int(input())

while people:
    for _ in range(step-1):
        person = people.popleft()
        people.append(person)
    removed_person = people.popleft()
    if people:
        print(f"Removed {removed_person}")
    else:
        print(f"Last is {removed_person}")