def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        people[name] = 0

    for name_letter, age in kwargs.items():
        for name in people.keys():
            if name[0] == name_letter:
                people[name] = age

    return people




print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
