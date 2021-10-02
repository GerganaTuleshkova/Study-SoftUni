import os.path

files = {}
# the traversed directory is the current directory. If another one is to be traversed the path should be changed below:
current_directory_path = os.getcwd()

for root, _, files_names in os.walk(current_directory_path):
    for file in files_names:
        file_extension = file.split(".")[-1]
        if file_extension not in files:
            files[file_extension] = []
        files[file_extension].append(file)

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
files = sorted(files.items(), key=lambda x: -len(x[1]))
output_file = open(f"{desktop}\\report.txt", "a")
for extension, file_names_list in files:
    output_file.write(f".{extension}\n")

    for file_name in file_names_list:
        output_file.write(f"---{file_name}\n")

output_file.close()
