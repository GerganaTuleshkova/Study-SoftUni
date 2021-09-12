def user_in_lists(book_dict, ussr):
    for user_list in book_dict.values():
        if user in user_list:
            return True
    return False


def initial_join_side(book, side, user):
    if side not in book and  not user_in_lists(book, user):
        book[side] = []
        book[side].append(user)
    elif not user_in_lists(book, user):
        book[side].append(user)

def remove_user_from_side(book, user):
    for (s, u) in book.items():
        if user in u:
            book[s].remove(user)


def join_existing_side(book, side, user):
    if side not in book and not user_in_lists(book, user):
        book[side] = []
        book[side].append(user)
    elif not user_in_lists(book, user):
        if side not in book:
            book[side] = []
        book[side].append(user)
    elif user_in_lists(book, user):
        if side not in book:
            book[side] = []
        remove_user_from_side(book, user)
        book[side].append(user)


command = input()
book = {}

while not command == "Lumpawaroo":
    if "|" in command:
        info = command.split(" | ")
        user, side = info[1], info[0]
        user_not_found = True
        initial_join_side(book, side, user)

    elif " -> " in command:
        info = command.split(" -> ")
        user, side = info[0], info[1]
        join_existing_side(book, side, user)
        print(f"{user} joins the {side} side!")

    command = input()



sorted_book = sorted(book.items(), key=lambda kpv: (-len(kpv[1]), kpv[0]))
for k, v in sorted_book:
    if len(v) > 0:
        print(f"Side: {k}, Members: {len(v)}")
        for u in sorted(v):
            print(f"! {u}")