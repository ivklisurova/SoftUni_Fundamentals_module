target_log = {}

while True:
    args = input()
    if args == 'Sail':
        break
    args = args.split('||')
    town = args[0]
    population = int(args[1])
    gold = int(args[2])
    if town not in target_log:
        target_log[town] = [population, gold]
    else:
        target_log[town][0] += population
        target_log[town][1] += gold

while True:
    tokens = input()
    if tokens == 'End':
        break
    tokens = tokens.split('=>')
    command = tokens[0]
    city = tokens[1]
    if command == 'Plunder':
        people = int(tokens[2])
        money = int(tokens[3])
        if city in target_log:
            target_log[city][0] -= people
            target_log[city][1] -= money
            print(f'{city} plundered! {money} gold stolen, {people} citizens killed.')
            if target_log[city][0] <= 0 or target_log[city][1] <= 0:
                print(f'{city} has been wiped off the map!')
                target_log.pop(city)

    elif command == 'Prosper':
        money = int(tokens[2])
        if money > 0:
            target_log[city][1] += money
            print(f'{money} gold added to the city treasury. {city} now has {target_log[city][1]} gold.')
        elif money < 0:
            print(f'Gold added cannot be a negative number!')

sorted_target_log = dict(sorted(target_log.items(), key=lambda x: (-x[1][1], x[0])))

if len(sorted_target_log) > 0:
    print(f'Ahoy, Captain! There are {len(sorted_target_log)} wealthy settlements to go to:')
    for k,v in sorted_target_log.items():
        print(f'{k} -> Population: {v[0]} citizens, Gold: {v[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
