pirate_ships = list(map(int, input().split('>')))
battle_ships = list(map(int, input().split('>')))

maximum_health = int(input())
stalemate = True

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Retire':
        break
    elif command == 'Fire':
        index = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= index < len(battle_ships):
            battle_ships[index] -= damage
            if battle_ships[index] <= 0:
                stalemate = False
                print('You won! The enemy ship has sunken.')
                break
    elif command == 'Defend':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        damage = int(tokens[3])
        if 0 <= start_index < len(pirate_ships) and 0 <= end_index < len(pirate_ships):
            for i, j in enumerate(pirate_ships[start_index:end_index + 1]):
                pirate_ships[i] -= damage
                if pirate_ships[i] <= 0:
                    stalemate = False
                    print('You lost! The pirate ship has sunken.')
                    break

    elif command == 'Repair':
        index = int(tokens[1])
        health = int(tokens[2])
        if 0 <= index < len(pirate_ships):
            if (pirate_ships[index] + health) < maximum_health:
                pirate_ships[index] += health
            else:
                pirate_ships[index] = maximum_health

    elif command == 'Status':
        counter = 0
        for i in pirate_ships:
            if i < maximum_health * 0.2:
                counter += 1
        print(f'{counter} sections need repair.')

if stalemate:
    print(f'Pirate ship status: {sum(pirate_ships)}')
    print(f'Warship status: {sum(battle_ships)}')

