def join_jump(string, list_names):
    tokens = string.split()
    command = tokens[0]
    name = tokens[1]
    if command == 'Join':
        list_names.append(name)
    elif command == 'Jump':
        idx = int(tokens[2])
        if len(list_names) > idx >= 0:
            list_names.insert(idx, name)
    return list_names


def dive(string, list_names):
    tokens = string.split()
    command = tokens[0]
    idx = int(tokens[1])
    if command == 'Dive':
        if len(list_names) > idx >= 0:
            list_names.pop(idx)
    return list_names


def count(string, list_names):
    tokens = string.split()
    line = tokens[0]
    counted_out = int(tokens[1])

    is_valid = False
    if len(list_names) > counted_out:
        is_valid = True

    if is_valid:
        if line == 'First':
            first = list_names[:counted_out]
            for x in first:
                print(x, end=' ')
        elif line == 'Last':
            start_element = len(list_names) - counted_out
            last = list_names[start_element:]
            for j in last:
                print(j, end=' ')
    else:
        for i in list_names:
            print(i, end=' ')


def print_output(string, list_names):
    tokens = string.split()
    direction = tokens[1]
    print('\nFrogs:', end=' ')
    if direction == 'Normal':
        for i in list_names:
            print(i, end=' ')
    elif direction == 'Reversed':
        reversed_list_names = list_names[::-1]
        for j in reversed_list_names:
            print(j, end=' ')


frogs = input().split()

while True:
    command = input()
    if command.startswith('Print'):
        print_output(command, frogs)
        break
    elif command.startswith('Join'):
        join_jump(command, frogs)
    elif command.startswith('Jump'):
        join_jump(command, frogs)
    elif command.startswith('Dive'):
        dive(command, frogs)
    elif command.startswith('First') or command.startswith('Last'):
        count(command, frogs)
