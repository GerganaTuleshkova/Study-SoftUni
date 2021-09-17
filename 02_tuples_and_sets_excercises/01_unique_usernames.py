num = int(input())

usernames = set()

for _ in range(num):
    username = input()
    usernames.add(username)

[print(name) for name in usernames]