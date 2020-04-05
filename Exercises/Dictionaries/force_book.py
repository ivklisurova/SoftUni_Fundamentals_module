user_log = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    try:
        side, user = command.split(' | ')
        if side not in user_log:
            user_log[side] = []
        if user not in user_log[side]:
            user_log[side].append(user)
    except:
        user, side = command.split(' -> ')
        a = user_log.values()
        ref_values = [x for x in a]
        if user in ref_values:
            user_log.pop(user)




