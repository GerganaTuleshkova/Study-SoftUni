class Party:

    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.people.append(name)
        return self.people

    def show_details(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


my_party = Party()

name = input()
while not name == "End":
    my_party.add_people(name)
    name = input()

print(my_party.show_details())