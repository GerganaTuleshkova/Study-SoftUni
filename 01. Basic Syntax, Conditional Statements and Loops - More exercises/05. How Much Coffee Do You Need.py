command = input()
coffee_count = 0

while not command == "END":
    if command.lower() in ["coding", "cat", "dog", "movie"]:
        if command.islower():
            coffee_count += 1
        if command.isupper():
            coffee_count += 2
    command = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)