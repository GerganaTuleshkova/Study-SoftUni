start_of_range = ord(input())
end_of_range = ord(input())
sum = 0
given_text = input()

for ch in given_text:
    if  start_of_range < ord(ch) < end_of_range:
        sum += ord(ch)

print(sum)

