courses = {}

while True:
    command = input()
    if command == 'end':
        break
    course, name = command.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(name)

courses = dict(sorted(courses.items(), key=lambda x: (len(x[1]), x[1].sort()), reverse=True))

for k, v in courses.items():
    print(f'{k}: {len(v)}')
    for i in courses[k]:
        print(f'-- {i}')
