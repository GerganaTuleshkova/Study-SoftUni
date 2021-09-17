n = int(input())

odd_results = set()
even_results = set()
row = 1
for _ in range(n):
    name = input()
    sum_of_ch = sum([ord(ch) for ch in name])
    result = sum_of_ch // row
    if result % 2 == 0:
        even_results.add(result)
    else:
        odd_results.add(result)
    row += 1

sum_odd = sum(odd_results)
sum_even = sum(even_results)

if sum_odd == sum_even:
    union = odd_results.union(even_results)
    print(", ".join(str(n) for n in union))

elif sum_odd > sum_even:
    difference = odd_results.difference(even_results)
    print(", ".join(str(n) for n in difference))

else:
    sym_difference = odd_results.symmetric_difference(even_results)
    print(", ".join(str(n) for n in sym_difference))

