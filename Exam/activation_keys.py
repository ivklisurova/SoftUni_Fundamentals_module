raw_key = input()

while True:
    args = input()
    if args == 'Generate':
        print(f'Your activation key is: {raw_key}')
        break
    args = args.split('>>>')
    command = args[0]
    if command == 'Contains':
        substring = args[1]
        if substring in raw_key:
            print(f'{raw_key} contains {substring}')
        else:
            print('Substring not found!')

    elif command == 'Flip':
        action = args[1]
        start_idx = int(args[2])
        end_idx = int(args[3])
        substring = raw_key[start_idx:end_idx]
        if action == 'Upper':
            raw_key = raw_key.replace(substring, substring.upper())
        elif action == 'Lower':
            raw_key = raw_key.replace(substring, substring.lower())
        print(raw_key)
    elif command == 'Slice':
        start_idx = int(args[1])
        end_idx = int(args[2])
        raw_key = raw_key.replace(raw_key[start_idx:end_idx], '')
        print(raw_key)
