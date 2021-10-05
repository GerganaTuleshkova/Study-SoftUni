def permute(index, values):
    if index == len(values):
        print(''.join(values))
        return
    for i in range(index, len(values)):
        values[i], values[index] = values[index], values[i]
        permute(index + 1, values)
        values[i], values[index] = values[index], values[i]


def permutation(word):
    if len(word) == 1:
        return [word]

    perms = permutation(word[1:])
    first_char = word[0]
    results = []

    for perm in perms:
        for i in range(len(perm)+1):

            results.append(perm[:i] + first_char + perm[i:])
            print((perm[:i] + first_char + perm[i:]))

    return results

print(permutation("abc"))