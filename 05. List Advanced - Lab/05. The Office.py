employees_hapiness = input().split()
factor = int(input())

happiness_factorred = list(map(lambda x: int(x) * factor, employees_hapiness))
happy_count = list(filter(lambda x: x >= (sum(happiness_factorred)/ len(happiness_factorred)), happiness_factorred))

if len(happy_count) >= len(happiness_factorred)/2:
    print(f"Score: {len(happy_count)}/{len(happiness_factorred)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(happiness_factorred)}. Employees are not happy!")