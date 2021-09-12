time_for_step_list = input().split()
time_steps = [int(x) for x in time_for_step_list]

left_time = 0
right_time = 0

for time in time_steps[:len(time_steps)//2]:
    if time == 0:
        left_time *= 0.80
    else:
        left_time += time

for time in time_steps[-1:(len(time_steps)//2):-1]:
    if time == 0:
        right_time *= 0.80
    else:
        right_time += time
winner = ""
total_time = 0
if left_time < right_time:
    winner = "left"
    total_time = left_time

else:
    winner = "right"
    total_time = right_time
print(f"The winner is {winner} with total time: {total_time:.1f}")