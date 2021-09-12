words = [el.lower() for el in input().split()]

my_dict = {}

for word in words:
    if word not in my_dict:
        my_dict[word] = 1
    else:
        my_dict[word] += 1

for key, value in my_dict.items():
    if not value % 2 == 0:
        print(key, end=" ")