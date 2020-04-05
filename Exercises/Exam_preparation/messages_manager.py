capacity = int(input())

message_log = {}

while True:
    args = input().split('=')
    command = args[0]
    if command == "Add":
        username = args[1]
        sent = int(args[2])
        received = int(args[3])
        if username not in message_log:
            message_log[username] = [sent,received]
    elif command == 'Message':
        sender = args[1]
        receiver = args[2]
        if sender in message_log and receiver in message_log:
            message_log[sender] += 1
            if message_log[sender] == capacity:
                print(f'{sender} reached the capacity!')
                message_log.pop(sender)
            message_log[receiver] += 1
            if message_log[receiver] == capacity:
                print(f'{receiver} reached the capacity!')
                message_log.pop(receiver)
    elif command == 'Empty':
        username = args[1]
        if username != 'All':
            message_log.pop(username)
        else:
            message_log.clear()
    elif command == 'Statistics':
        break

sorted_message_log = dict(sorted(message_log.items(),key=lambda x: (-x[1],x[0])))

print(f'Users count: {len(sorted_message_log)}')

for k,v in sorted_message_log.items():
    print(f'{k} - {v}')