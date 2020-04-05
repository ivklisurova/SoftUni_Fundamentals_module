email = input()

while True:
    args = input().split(' ')
    command = args[0]
    if command == 'Complete':
        break
    if command == 'Make':
        if args[1] == 'Upper':
            email = email.upper()
        elif args[1] == 'Lower':
            email = email.lower()
        print(email)
    elif command == 'GetDomain':
        count = int(args[1])
        print(email[len(email) - count:])
    elif command == 'GetUsername':
        if '@' in email:
            idx = email.find('@')
            print(email[:idx])
        else:
            print(f'The email {email} doesn\'t contain the @ symbol.')
    elif command == 'Replace':
        char = args[1]
        email = email.replace(char, '-')
        print(email)
    elif command == 'Encrypt':
        [print(ord(i), end=' ') for i in email]
