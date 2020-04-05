n = int(input())

parking_log = {}

for i in range(0, n):
    tokens = input().split()
    command = tokens[0]
    username = tokens[1]

    if command == 'register':
        plate = tokens[2]
        if username not in parking_log:
            parking_log[username] = plate
            print(f'{username} registered {plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking_log[username]}')

    elif command == 'unregister':
        if username not in parking_log:
            print(f'ERROR: user {username} not found')
        else:
            parking_log.pop(username)
            print(f'{username} unregistered successfully')

[print(f'{k} => {v}') for k, v in parking_log.items()]
