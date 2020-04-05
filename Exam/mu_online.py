dungeons_rooms = input().split('|')

INITIAL_HEALTH = 100

health = 100
bitcoins = 0
best_room = 0
is_dead = False

for i in dungeons_rooms:
    tokens = i.split(' ')
    command = tokens[0]
    args = int(tokens[1])
    best_room += 1
    if command == 'potion':
        if health + args < INITIAL_HEALTH:
            health += args
            print(f'You healed for {args} hp.')
        else:
            diff = INITIAL_HEALTH - health
            health = INITIAL_HEALTH
            print(f'You healed for {diff} hp.')

        print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcoins += args
        print(f'You found {args} bitcoins.')
    else:
        health -= args
        if health > 0:
            print(f'You slayed {command}.')
        elif health <= 0:
            print(f'You died! Killed by {command}.')
            is_dead = True
            print(f'Best room: {best_room}')
            break

if not is_dead:
    print(f'You\'ve made it!\nBitcoins: {bitcoins}\nHealth: {health}')


