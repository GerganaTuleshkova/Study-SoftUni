list_of_coded_words = input().split("|")

morse_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
              'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..'}
decoded_text = []
for word in list_of_coded_words:
    letters = word.split(" ")
    decoded_word = ""
    for letter in letters:
        if letter in morse_dict.values():
            for regular_letter, morse_letter in morse_dict.items():
                if letter == morse_letter:
                    decoded_letter = regular_letter
            decoded_word += decoded_letter
    decoded_text.append(decoded_word)

print(" ".join(decoded_text))


