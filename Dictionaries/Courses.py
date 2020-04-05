students_log = {}

while True:
    command = input()
    if command == 'end':
        break
    tokens = command.split(' : ')
    course = tokens[0]
    student_name = tokens[1]

    if course not in students_log:
        students_log[course] = []
        students_log[course].append(student_name)
    else:
        students_log[course].append(student_name)


students_log = dict(sorted(students_log.items(),key=lambda x: (len(x[1]), x[1].sort()),reverse=True))

for k,v in students_log.items():
    print(f'{k}: {len(v)}')
    for i in students_log[k]:
        print(f'-- {i}')

