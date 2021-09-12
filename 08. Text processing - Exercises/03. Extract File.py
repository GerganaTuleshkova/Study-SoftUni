path_as_list = input().split("\\")

file = path_as_list[-1]
file_name, file_extension = file.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
