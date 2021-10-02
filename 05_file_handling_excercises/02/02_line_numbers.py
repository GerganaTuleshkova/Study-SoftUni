import string

file = open("text.txt", "r")
output_file = open("output.txt", "w")
punctuations = string.punctuation
count = 1

for line in file:
    punctuation_count = 0
    letters_count = 0
    for ch in line:
        if ch in punctuations:
            punctuation_count += 1
        elif ch.isalpha():
            letters_count += 1
    output_line = f"Line {count}: {line.strip()} ({letters_count})({punctuation_count})\n"
    output_file.write(output_line)
    count += 1

file.close()
output_file.close()
