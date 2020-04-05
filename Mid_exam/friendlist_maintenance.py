friends = input().split(', ')

while True:
    count_lost = friends.count('Lost')
    count_blacklisted = friends.count('Blacklisted')
    command = input().split()
    if command[0] == 'Report':
        print(f'Blacklisted names: {count_blacklisted}\nLost names: {count_lost}')
        break
    elif command[0] == 'Blacklist':
        name = command[1]
        if name in friends:
            for i, j in enumerate(friends):
                if j == name:
                    print(f'{name} was blacklisted.')
                    friends[i] = 'Blacklisted'
        else:
            print(f'{name} was not found.')
    elif command[0] == 'Error':
        index = int(command[1])
        if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
            print(f'{friends[index]} was lost due to an error.')
            friends[index] = 'Lost'
    elif command[0] == 'Change':
        idx = int(command[1])
        new_name = command[2]
        if 0 <= idx < len(friends):
            print(f'{friends[idx]} changed his username to {new_name}.')
            friends[idx] = new_name

[print(i,end=' ') for i in friends]