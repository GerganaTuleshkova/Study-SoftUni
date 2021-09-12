num_of_pieces = int(input())

pieces_dict = {}

for n in range(num_of_pieces):
    info = input().split("|")
    piece = info[0]
    composer = info[1]
    key = info[2]
    pieces_dict[piece] = {"composer": composer, "key": key}

command = input()

while not command == "Stop":
    instructions = command.split("|")
    action = instructions[0]
    piece_name = instructions[1]
    if action == "Add":
        composer_to_add = instructions[2]
        key_to_add = instructions[3]
        if piece_name in pieces_dict:
            print(f"{piece_name} is already in the collection!")
        else:
            pieces_dict[piece_name] = {"composer": composer_to_add, "key": key_to_add}
            print(f"{piece_name} by {composer_to_add} in {key_to_add} added to the collection!")
    elif action == "Remove":
        if piece_name in pieces_dict:
            print(f"Successfully removed {piece_name}!")
            del pieces_dict[piece_name]
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = instructions[2]
        if piece_name in pieces_dict:
            pieces_dict[piece_name]["key"] = new_key
            print(f"Changed the key of {piece_name} to {new_key}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    command = input()

ordered_pieces = sorted(pieces_dict.items(), key=lambda kvp: (kvp[0], kvp[1]["composer"]))

for name, details in ordered_pieces:
    print(f"{name} -> Composer: {details['composer']}, Key: {details['key']}")