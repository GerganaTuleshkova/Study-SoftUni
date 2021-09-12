import re

racers_names = input().split(", ")
racers_results_by_name = {}

info = input()

pattern_names = r"[A-Za-z]"
pattern_score = r"\d"
while not info == "end of race":
    letters = re.findall(pattern_names, info)
    digits = re.findall(pattern_score, info)
    name_extracted = ""
    for letter in letters:
        name_extracted += letter
    score = 0
    for digit in digits:
        score += int(digit)

    if name_extracted in racers_names:
        if name_extracted not in racers_results_by_name:
            racers_results_by_name[name_extracted] = score
        else:
            racers_results_by_name[name_extracted] += score

    info = input()

racers_results_by_name = sorted(racers_results_by_name.items(), key=lambda x: -(x[1]))
if len(racers_results_by_name) >= 3:
    print(f"1st place: {racers_results_by_name[0][0]}")
    print(f"2nd place: {racers_results_by_name[1][0]}")
    print(f"3rd place: {racers_results_by_name[2][0]}")