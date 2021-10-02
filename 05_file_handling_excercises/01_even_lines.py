characters_to_replace = ["-", ",", ".", "!", "?"]
file = open("text.txt", "r")

count = 0
for line in file:
    if count % 2 == 0:
        for symbol in characters_to_replace:
            line = line.replace(symbol, "@")
        line = line.split()[:: -1]
        print(" ".join(line))
    count += 1

file.close()