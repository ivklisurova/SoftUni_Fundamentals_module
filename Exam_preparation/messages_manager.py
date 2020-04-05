from operator import itemgetter

capacity = int(input())

message_manager = {}

while True:
    user_input = input()
    if user_input == 'Statistics':
        break
    tokens = user_input.split('=')

    command = tokens[0]

    if command == 'Add':
        username = tokens[1]
        sent = int(tokens[2])
        received = int(tokens[3])
        if username not in message_manager:
            message_manager[username] = []
            message_manager[username].append(sent)
            message_manager[username].append(received)
    elif command == 'Message':
        sender = tokens[1]
        receiver = tokens[2]
        if sender in message_manager and receiver in message_manager:
            message_manager[sender][0] += 1
            message_manager[receiver][1] += 1

            if message_manager[sender][0] + message_manager[sender][1] == capacity:
                message_manager.pop(sender)
                print(f'{sender} reached the capacity!')
            elif message_manager[receiver][0] + message_manager[receiver][1] == capacity:
                message_manager.pop(receiver)
                print(f'{receiver} reached the capacity!')
    elif command == 'Empty':
        username = tokens[1]
        if username == 'All':
            message_manager.clear()
        else:
            message_manager.pop(username)

users_count = len(message_manager)
print(f'Users count: {users_count}')

message_log = dict(sorted(message_manager.items(),key=lambda x: (-x[1][1],x[0])))
messages_score = {}
for x, y in message_log.items():
    value = 0
    for i in y:
        value += i
    messages_score[x] = value

[print(f'{name} - {logs}') for name, logs in messages_score.items()]
