n = int(input())

parking_log = {}

for i in range(n):
    tokens = input().split(' ')
    command = tokens[0]
    username = tokens[1]
    if command == 'register':
        license_plate = tokens[2]
        if username not in parking_log:
            parking_log[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking_log[username]}')
    elif command == 'unregister':
        if username not in parking_log:
            print(f'ERROR: user {username} not found')
        else:
            parking_log.pop(username)
            print(f'{username} unregistered successfully')

[print(f'{k} => {v}') for k, v in parking_log.items()]
