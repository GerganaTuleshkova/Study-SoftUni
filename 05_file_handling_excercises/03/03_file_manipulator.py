import os.path

command = input()

while not command == "End":
    command_args = command.split("-")
    action, file_name = command_args[:2]
    if action == "Create":
        open(file_name, "w").close()
    elif action == "Add":
        content_to_add = command_args[2]
        with open(file_name, "a") as file:
            file.write(content_to_add)
            file.write("\n")
    elif action == "Replace":
        old_string, new_string = command_args[2:]
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            with open(file_name, "r+") as file:
                text_in_file = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(text_in_file)
    elif action == "Delete":
        if not os.path.exists(file_name):
            print("An error occurred")
        else:
            os.remove(file_name)

    command = input()