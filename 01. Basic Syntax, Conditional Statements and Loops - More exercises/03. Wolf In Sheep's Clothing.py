given_string = input()
queue1 = given_string.replace(" ", "")

queue = queue1.split(",")

# print(queue)
# print(queue.index("wolf"))
# print(len(queue))
number = len(queue) - queue.index("wolf") - 1
if queue.index("wolf") == len(queue) - 1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {number}! You are about to be eaten by a wolf!")