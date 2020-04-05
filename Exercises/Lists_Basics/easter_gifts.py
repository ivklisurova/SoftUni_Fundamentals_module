presents = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    command = command.split()
    gift = command[1]
    if command[0] == 'OutOfStock':
        for i, j in enumerate(presents):
            if j == gift:
                presents[i] = 'None'
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 <= index < len(presents):
            presents[index] = gift

    elif command[0] == 'JustInCase':
        if len(presents) > 0:
            presents[-1] = gift

[print(present, end=' ') for present in presents if present != 'None']
