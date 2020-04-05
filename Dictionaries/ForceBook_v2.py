user_log = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    tokens = command.split(' | ')

    if len(tokens) == 2:
        side, user = tokens[0], tokens[1]
        if side not in user_log:
            user_log[side] = []
            user_log[side].append(user)
        else:
            if user not in user_log[side]:
                user_log[side].append(user)
    else:
        user, side = command.split(' -> ')

        for k, v in user_log.items():
            for i in user_log[k]:
                if i == user:
                    a = user_log[k].index(user)
                    user_log[k].pop(a)
                    user_log[side].append(user)

        if user not in user_log[side]:
            user_log[side].append(user)

        print(f'{user} joins the {side} side!')

user_log = dict(sorted(user_log.items(),key=lambda x:(len(x[1]),x[0],x[1].sort())))

for k,v in user_log.items():
    members = len(v)
    if members == 0:
        continue
    else:
        print(f'Side: {k}, Members: {len(v)}')
        for i in user_log[k]:
            print(f'! {i}')