actions = [0] * 11

command = input()
while not command == "End":
    to_do_notes = command.split("-")
    priority = int(to_do_notes[0])
    action = to_do_notes[1]
    actions.pop(priority)
    actions.insert(priority, action)
    command = input()

print([x for x in actions if x != 0])
