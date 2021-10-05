def generate01(vector, index):
    if index == len(vector):
        print(" ".join([str(x) for x in vector]))
        return

    for number in range(2):
        vector[index] = number
        generate01(vector, index + 1)


vector = [None]*8
generate01(vector, 0)
