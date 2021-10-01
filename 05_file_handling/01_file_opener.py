import os.path

file_name = "text.txt"
if os.path.isfile(file_name):
    print("File found")
    open(file_name)
else:
    print("File not found")

# second option
try:
    file = open(file_name, "r")
    print("File found")
except FileNotFoundError:
    print("File not found")