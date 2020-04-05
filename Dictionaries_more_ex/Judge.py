from operator import itemgetter

judge_log = {}
individual_log = {}

while True:
    command = input()
    if command == 'no more time':
        break
    tokens = command.split(' -> ')
    username = tokens[0]
    contest = tokens[1]
    points = int(tokens[2])
    if contest not in judge_log:
        judge_log[contest] = {}
        judge_log[contest][username] = [points]
        if username not in individual_log:
            individual_log[username] = points
    else:
        if username in judge_log[contest]:
            if points > judge_log[contest][username][0]:
                current_points = judge_log[contest][username].pop(0)
                individual_log[username] -= current_points
                judge_log[contest][username].append(points)
                individual_log[username] += points
        else:
            judge_log[contest][username] = [points]
            if username not in individual_log:
                individual_log[username] = 0
            individual_log[username] += points

individual_log = dict(sorted(individual_log.items(), key=itemgetter(1, 0), reverse=True))
my_sorted = {key:sorted(values, key=lambda x:x[1]) for key,values in judge_log.items()}

for k, v in judge_log.items():
    print(f'{k}: {len(v)} participants')
    position = 1
    for a,b in v.items():
        print(f'{position}. {a} <::> {"".join(str(b))}')
        position += 1

print('Individual standings:')

individual_ranking = 1

for k, v in individual_log.items():
    print(f'{individual_ranking}. {k} -> {v}')
    individual_ranking += 1
