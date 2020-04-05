username = input()

while True:
    command = input()
    if command == 'Sign up':
        break
    tokens = command.split()
    action = tokens[0]

    if action == 'Case':
        if tokens[1] == 'lower':
            username = username.lower()
        elif tokens[1] == 'upper':
            username = username.upper()
        print(username)
    elif action == 'Reverse':
        start_idx = int(tokens[1])
        end_idx = int(tokens[2])
        if start_idx > len(username) or end_idx > len(username):
            continue
        sub_string = username[start_idx:end_idx + 1]
        print(sub_string[::-1])
    elif action == 'Cut':
        substring = tokens[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    elif action == 'Replace':
        ch = tokens[1]
        username = username.replace(ch,'*')
        print(username)
    elif action == 'Check':
        char = tokens[1]
        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')


