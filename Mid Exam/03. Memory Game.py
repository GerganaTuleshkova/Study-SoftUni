def is_not_valid_index(collection, index):
    if 0 <= index < len(collection):
        return False
    return True



sequence = input().split()
moves = 0

attempt = input()

while not attempt == "end":
    indices = [int(n) for n in attempt.split()]
    moves += 1
    index_1, index_2 = indices[0], indices[1]
    if index_1 == index_2 or is_not_valid_index(sequence, index_1) or is_not_valid_index(sequence, index_2):
        el_to_add = f"-{moves}a"
        index_to_add = int(len(sequence)/2)
        sequence.insert(index_to_add, el_to_add)
        sequence.insert(index_to_add, el_to_add)
        print("Invalid input! Adding additional elements to the board")
    elif sequence[index_1] == sequence[index_2]:
        matching_el = sequence[index_1]
        print(f"Congrats! You have found matching elements - {matching_el}!")
        sequence.remove(matching_el)
        sequence.remove(matching_el)
    elif not sequence[index_1] == sequence[index_2]:
        print("Try again!")
    if not sequence:
        print(f"You have won in {moves} turns!")
        break

    attempt = input()

if sequence:
    print("Sorry you lose :(")
    print(" ".join(sequence))

