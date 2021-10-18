from collections import deque


jobs = deque([int(x) for x in input().split(", ")])
searched_index = int(input())

cycles_waited = 0
jobs_by_length = {}

for index in range(len(jobs)):
    if jobs[index] not in jobs_by_length:
        jobs_by_length[jobs[index]] = []
    jobs_by_length[jobs[index]].append(index)

index_found = False
for job_length, indices in sorted(jobs_by_length.items()):
    for index in indices:
        cycles_waited += job_length
        if index == searched_index:
            index_found = True
            break

    if index_found:
        break

print(cycles_waited)



