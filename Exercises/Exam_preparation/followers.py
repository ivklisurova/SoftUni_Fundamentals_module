log = {}

while True:
    args = input()
    if args == 'Log out':
        break
    args = args.split(':')
    command = args[0]
    username = args[1]
    if command == 'New follower':
        if username not in log:
            log[username] = 0
    elif command == 'Like':
        count = int(args[2])
        if username not in log:
            log[username] = 0
        log[username] += count
    elif command == 'Comment':
        if username not in log:
            log[username] = 0
        log[username] += 1
    elif command == 'Blocked':
        if username in log:
            log.pop(username)
        else:
            print(f'{username} doesn\'t exist.')

sorted_log = dict(sorted(log.items(), key=lambda x: (-(x[1]), x[0])))

print(f'{len(sorted_log)} followers')
[print(f'{k}: {v}') for k, v in sorted_log.items()]


