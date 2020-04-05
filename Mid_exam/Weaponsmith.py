parts = input().split('|')

while True:
    command = input().split()
    if command[0] == 'Done':
        print(f'You crafted {"".join(parts)}!')
        break

    elif command[0] == 'Move':
        idx = int(command[2])
        length_list = len(parts)
        if command[1] == 'Left':
            if (idx - 1) < 0:
                continue
            try:
                element = parts.pop(idx)
                parts.insert(idx - 1, element)
            except IndexError:
                continue

        elif command[1] == 'Right':
            if idx + 1 > length_list:
                continue
            try:
                element = parts.pop(idx)
                parts.insert(idx + 1, element)
            except IndexError:
                continue

    elif command[0] == 'Check':
        what_to_check = command[1]
        if what_to_check == 'Even':
            [print(j, end=' ') for i, j in enumerate(parts) if i % 2 == 0]
            print()
        elif what_to_check == 'Odd':
            [print(j, end=' ') for i, j in enumerate(parts) if i % 2 != 0]
            print()
