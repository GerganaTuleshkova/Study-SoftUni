command = input()
users = {}

while not command == "End":
    info = command.split(" -> ")
    company, employee = info[0], info[1]
    if company not in users:
        users[company] = []
    if employee not in users[company]:
        users[company].append(employee)
    command = input()
users = dict(sorted(users.items()))

for c, employees in users.items():
    print(c)
    for e in (employees):
        print(f"-- {e}")