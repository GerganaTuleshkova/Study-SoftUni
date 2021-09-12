given_string = input()
shuffles = int(input())

deck = given_string.split(" ")

for _ in range(shuffles):
    half_1 = deck[1:int(len(deck) / 2)]
    half_2 = deck[int(len(deck)/2):-1]
    middle = []
    for i in range(len(half_1)):
        middle.append(half_2[i])
        middle.append(half_1[i])
    deck[1:len(deck)-1] = middle

print(deck)
