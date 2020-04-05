emails_log = {}

while True:
    args = input().split('->')
    command = args[0]
    if command == 'Statistics':
        break
    username = args[1]
    if command == 'Add':
        if username not in emails_log:
            emails_log[username] = []
        else:
            print(f'{username} is already registered')
    elif command == 'Send':
        email = args[2]
        if username in emails_log:
            emails_log[username].append(email)
    elif command == 'Delete':
        if username in emails_log:
            emails_log.pop(username)
        else:
            print(f'{username} not found!')

sorted_email_log = dict(sorted(emails_log.items(), key=lambda x: (-len(x[1]), x[0])))

print(f'Users count: {len(sorted_email_log)}')

for k in sorted_email_log:
    print(k)
    for x in sorted_email_log[k]:
        print(f'- {x}')
