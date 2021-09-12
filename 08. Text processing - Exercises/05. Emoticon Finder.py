# text_as_list = input().split(":")
# print(text_as_list)
# # if len(text_as_list) > 1:
# #     for i in text_as_list[1:]:
# #         print(f":{i[0]}")

text = input()

for i in range(0, len(text)):
    if text[i] == ":":
        print(f":{text[i+1]}")