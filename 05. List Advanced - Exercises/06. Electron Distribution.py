electron_number = int(input())

all_shells = [2*n**2 for n in range(1, electron_number)]
filled_shells = []


for shell in all_shells:
    if electron_number >= 0:
        if electron_number >= shell:
            filled_shells.append(shell)
        else:
            filled_shells.append(electron_number)
        electron_number -= shell
    else:
        break


print(filled_shells)
