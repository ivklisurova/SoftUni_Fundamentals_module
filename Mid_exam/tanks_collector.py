vehicles = input().split(', ')
n = int(input())

for i in range(n):
    tokens = input().split(', ')
    command = tokens[0]

    if command == 'Add':
        tank_name = tokens[1]
        if tank_name in vehicles:
            print('Tank is already bought')
        else:
            vehicles.append(tank_name)
            print('Tank successfully bought')
    elif command == 'Remove':
        tank_name = tokens[1]
        if tank_name in vehicles:
            vehicles.remove(tank_name)
            print('Tank successfully sold')
        else:
            print('Tank not found')
    elif command == 'Remove At':
        index = int(tokens[1])
        if 0 <= index < len(vehicles):
            vehicles.pop(index)
            print('Tank successfully sold')
        else:
            print('Index out of range')
    elif command == 'Insert':
        index = int(tokens[1])
        tank_name = tokens[2]

        if 0 <= index < len(vehicles):
            if tank_name not in vehicles:
                vehicles.insert(index,tank_name)
                print('Tank successfully bought')
            else:
                print('Tank is already bought')

        else:
            print('Index out of range')


print(', '.join(vehicles))
