number = int(input())

for first_letter in range(97, 97 + number):
    for second_letter in range(97, 97 + number):
        for third_letter in range(97, 97 + number):
            print(chr(first_letter)+chr(second_letter) +chr(third_letter))