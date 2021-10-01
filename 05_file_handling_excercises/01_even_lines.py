characters_to_replace = ["-", ",", ".", "!", "?"]

file = open("text.txt", "r")

count = 0

for line in file:

    if count % 2 == 0:
        line = line.split()[:: -1]
        line = " ".join(line)
        line = list(line)
        for i in range(len(line)):
            if line[i] in characters_to_replace:
                line[i] = "@"

        print("".join(line))

    count += 1

file.close()