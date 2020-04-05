battle_log = {}

while True:
    args = input().split(':')
    command = args[0]
    if command == 'Results':
        break
    if command == 'Add':
        person_name = args[1]
        health = int(args[2])
        energy = int(args[3])
        if person_name not in battle_log:
            battle_log[person_name] = [health, energy]
        else:
            battle_log[person_name][0] += health
    elif command == 'Attack':
        attacker_name = args[1]
        defender_name = args[2]
        damage = int(args[3])
        if defender_name in battle_log and attacker_name in battle_log:
            battle_log[defender_name][0] -= damage
            if battle_log[defender_name][0] <= 0:
                print(f'{defender_name} was disqualified!')
                battle_log.pop(defender_name)
            battle_log[attacker_name][1] -= 1
            if battle_log[attacker_name][1] <= 0:
                print(f'{attacker_name} was disqualified!')
                battle_log.pop(attacker_name)
    elif command == 'Delete':
        username = args[1]
        if username == 'All':
            battle_log.clear()
        else:
            battle_log.pop(username)

sorted_battle_log = dict(sorted(battle_log.items(), key=lambda x: (-x[1][0], x[0])))

print(f'People count: {len(sorted_battle_log)}')

for k, v in sorted_battle_log.items():
    print(f'{k} - {v[0]} - {v[1]}')
