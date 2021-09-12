num_words = int(input())
dictionary = {}

for _ in range(num_words):
    key = input()
    value = input()
    if key not in dictionary:
        dictionary[key] = [value]
    else:
        dictionary[key].append(value)

for word, synonyms in dictionary.items():
    print(f"{word} - {(', '.join(synonyms))}")