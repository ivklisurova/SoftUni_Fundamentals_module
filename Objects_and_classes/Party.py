class Party:
    def __init__(self):
        self.people = []

    def go(self, name):
        self.people.append(name)

    def get_going(self):
        return f'Going: {", ".join(self.people)}'

    def get_count(self):
        return f'Total: {len(self.people)}'


party = Party()

while True:
    name_1 = input()
    if name_1 == 'End':
        break
    party.go(name_1)

print(party.get_going())
print(party.get_count())
