def show_loading_bar(number):
    if number == 100:
        print("100% Complete!")
    if number < 100:
        print(f"{number}% ", end="")
    loading_list = []
    for i in range(1, number//10 +1):
        loading_list.append("%")
    for rest in range(number//10+ 1, 11):
        loading_list.append(".")
    print("[", end="")
    print("".join(loading_list), end="")
    print("]", end="")
    if number < 100:
        print("\nStill loading...")


given_number = int(input())
show_loading_bar(given_number)