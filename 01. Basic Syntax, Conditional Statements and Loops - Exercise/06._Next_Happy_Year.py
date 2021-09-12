year = int(input())

new_happy_year = year +1
next_year_not_found = True
while next_year_not_found:
    digit1 = new_happy_year // 1000
    digit2 = (new_happy_year - digit1*1000) // 100
    digit3 = (new_happy_year - digit1* 1000 - digit2*100) // 10
    digit4 = new_happy_year - digit1* 1000 - digit2*100 - digit3*10

    if digit4 != digit3 and digit4 != digit2 and digit4 != digit1 and digit1 != digit2 and digit3 != digit2 and digit1 != digit3:
        next_year_not_found = False
        break
    else:
        new_happy_year += 1
print(new_happy_year)