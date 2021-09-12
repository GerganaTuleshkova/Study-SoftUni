number_snowballs = int(input())
highest_value = 0
highest_snow = 0
highest_time = 0
highest_quality = 0

for snowball in range(1, number_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if highest_value < snowball_value:
        highest_value = snowball_value
        highest_snow = snowball_snow
        highest_time = snowball_time
        highest_quality = snowball_quality

print(f"{highest_snow} : {highest_time} = {int(highest_value)} ({highest_quality})")