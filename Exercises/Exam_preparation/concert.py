concert_log = {}
time_log = {}

while True:
    args = input().split('; ')
    if args[0] == 'start of concert':
        break
    command = args[0]
    band = args[1]
    tokens = args[2].split(', ')
    if command == 'Add':
        if band not in concert_log:
            concert_log[band] = []
        if band not in time_log:
            time_log[band] = 0
        for i in tokens:
            if i not in concert_log[band]:
                concert_log[band].append(i)
    elif command == 'Play':
        time = int(tokens[0])
        if band not in time_log:
            time_log[band] = 0
        time_log[band] += time

top_band = input()

sorted_time_log = dict(sorted(time_log.items(), key=lambda x: (-x[1], x[0])))
total_time = sum(sorted_time_log.values())

print(f'Total time: {total_time}')

for k, v in sorted_time_log.items():
    print(f'{k} -> {v}')

print(top_band)
for x in concert_log[top_band]:
    print(f'=> {x}')
