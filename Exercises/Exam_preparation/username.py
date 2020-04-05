username = input()

while True:
    args = input().split(' ')
    command = args[0]
    if command == 'Sign':
        break
    if command == 'Case':
        if args[1] == 'lower':
            username = username.lower()
        elif args[1] == 'upper':
            username = username.upper()
        print(username)
    elif command == 'Reverse':
        start_idx = int(args[1])
        end_idx = int(args[2])
        if 0 <= start_idx and end_idx < len(username):
            substring = username[start_idx:end_idx+1]
            print(substring[::-1])
    elif command == "Cut":
        substring = args[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    elif command == 'Replace':
        char = args[1]
        username = username.replace(char, '*')
        print(username)
    elif command == 'Check':
        char = args[1]
        if char in username:
            print('Valid')
        else:
            print(f'Your username must contain {char}.')
