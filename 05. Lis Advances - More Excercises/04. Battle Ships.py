def shoot(collection: list, row: int, column: int):
    """Decreases the value of the ship at given row and column by 1. Returns the updated collection and the number
    of destroyed ships (1 ship if value of the ship dropped to 0, or 0 destroyed ships
    in case the value of the ship is above 0"""
    destroyed_ships = 0
    if collection[row][column] > 0:
        collection[row][column] -= 1
        if collection[row][column] == 0:
            destroyed_ships = 1
    return collection, destroyed_ships


rows = int(input())
field = []

for row in range(rows):
    ships_in_row = [int(ship) for ship in input().split()]
    field.append(ships_in_row)

shoots_input = [shot for shot in input().split()]
total_destroyed_ships = 0
for shoot_pair in shoots_input:
    shot = [int(s) for s in shoot_pair.split("-")]
    row = shot[0]
    index = shot[1]
    collection, destroyed_ships = shoot(field, row, index)
    field = collection
    total_destroyed_ships += destroyed_ships

print(total_destroyed_ships)