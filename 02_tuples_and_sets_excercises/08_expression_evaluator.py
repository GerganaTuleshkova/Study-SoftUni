from collections import deque

def make_calculation(queue, operator):
    if operator == "*":
        result = 1
        while queue:
            result *= queue.popleft()
        queue.append(result)
    elif operator == "+":
        result = 0
        while queue:
            result += queue.popleft()
        queue.append(result)
    elif operator == "-":
        if queue:
            result = queue.popleft()
            while queue:
                result -= queue.popleft()
            queue.append(result)
    elif operator == "/":
        if queue:
            result = queue.popleft()
            while queue:
                result //= queue.popleft()
            queue.append(result)
    return queue


given_string = input().split()
numbers = deque()


for ch in given_string:
    if ch in "*+-/":
        numbers = make_calculation(numbers, ch)
    else:
        numbers.append(int(ch))

print(numbers.popleft())
