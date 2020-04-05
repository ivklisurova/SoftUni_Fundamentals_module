exam_log = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break

    tokens = command.split('-')
    name = tokens[0]
    language = tokens[1]

    if language != 'banned':
        points = int(tokens[2])
        if name not in exam_log:
            exam_log[name] = points
        if points > exam_log[name]:
            exam_log[name] = points

        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    else:
        exam_log.pop(name)


exam_log = dict(sorted(exam_log.items(),key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(),key=lambda x: (-x[1], x[0])))

print('Results:')
[print(f'{k} | {v}') for k, v in exam_log.items()]

print('Submissions:')
[print(f'{k} - {v}') for k,v in submissions.items()]


