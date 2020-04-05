practice_log = {}

while True:
    tokens = input().split('->')
    command = tokens[0]
    if command == 'END':
        break

    elif command == 'Add':
        road = tokens[1]
        racer = tokens[2]
        if road not in practice_log:
            practice_log[road] = []
        if road in practice_log:
            practice_log[road].append(racer)
    elif command == 'Move':
        road = tokens[1]
        racer = tokens[2]
        next_road = tokens[3]
        if racer in practice_log[road]:
            practice_log[road].remove(racer)
            practice_log[next_road].append(racer)
    elif command == 'Close':
        road = tokens[1]
        practice_log.pop(road)

sorted_log = dict(sorted(practice_log.items(),key=lambda x: (-(len(x[1])),x[0]) ))


print('Practice sessions:')

for k in sorted_log:
    print(k)
    for v in sorted_log[k]:
        print(f'++{v}')