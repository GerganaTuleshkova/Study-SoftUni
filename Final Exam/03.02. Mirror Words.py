import re
text = input()

pattern = r"(?P<surrounding>[@|#])(?P<word_1>[a-zA-Z]{3,})(?P=surrounding){2}(?P<word_2>[a-zA-Z]{3,})(?P=surrounding)"
mirror_words = {}
pairs_iter = re.finditer(pattern, text)

if not re.search(pattern, text):
    print("No word pairs found!")

count_of_pairs = 0
for pair_match in pairs_iter:
    count_of_pairs += 1
    word_1 = pair_match.group("word_1")
    word_2 = pair_match.group("word_2")
    if word_1 == word_2[::-1]:
        mirror_words[word_1] = word_2
if not count_of_pairs == 0:
    print(f"{count_of_pairs} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    pairs = []
    for w_1, w_2 in mirror_words.items():
        pair = f"{w_1} <=> {w_2}"
        pairs.append(pair)
    print(", ".join(pairs))


