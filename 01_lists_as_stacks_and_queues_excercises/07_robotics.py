from collections import deque

robots_queue = deque()
robots_p_time_queue = deque()

information = input().split(";")
for info in information:
    robot_info = info.split("-")
    robots_queue.append(robot_info[0])
    robots_p_time_queue.append(int(robot_info[1]))

time = {"h": 0, "m": 0, "s": 0}
time_list = input().split(":")
time["h"] = time_list[0]
time["m"] = time_list[1]
time["s"] = time_list[2]

products_queue = deque()

while True:
    command = input()
    if command == "End":
        break
    else:
        products_queue.append(command)




print(robots_queue)
print(robots_p_time_queue)
print(time)
print(products_queue)