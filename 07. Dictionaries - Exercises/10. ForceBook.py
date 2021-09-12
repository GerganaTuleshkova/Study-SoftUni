command = input()
book = {}

while not command == "Lumpawaroo":
    if "|" in command:
        info = command.split(" | ")
        user, side = info[1], info[0]
        user_not_found = True
        for key in book.keys():
            if user not in book[key]:
                continue
            else:
                user_not_found = False
        if side not in book and user_not_found:
            book[side] = [user]
        elif side in book and user_not_found:
            book[side].append(user)

    elif " -> " in command:
        info = command.split(" -> ")
        user, side = info[0], info[1]
        user_not_found = True
        for key in book.keys():
            if user not in book[key]:
                continue
            else:
                user_not_found = False
                found_in_side = key
        if user_not_found:
            if side not in book:
                book[side] = []
            book[side].append(user)
        else:
            book[found_in_side].remove(user)
            book[side].append(user)
        print(f"{user} joins the {side} side!")

    command = input()

# book = dict(sorted(book.items()))
# book = dict(sorted(book.items(), key=lambda x: -len(x[1])))

sorted_book = sorted(book.items(), key=lambda kpv: (-len(kpv[1]), kpv[0]))
for k, v in sorted_book:
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for u in sorted(v):
            print(f"! {u}")