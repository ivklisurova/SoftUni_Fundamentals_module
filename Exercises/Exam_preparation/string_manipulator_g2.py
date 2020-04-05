string = input()

while True:
    args = input().split(' ')
    command = args[0]
    if command == 'Done':
        break
    if command == 'Change':
        char = args[1]
        replacement = args[2]
        string = string.replace(char, replacement)
        print(string)
    elif command == 'Includes':
        substring = args[1]
        if substring in substring:
            print('True')
        else:
            print('False')
    elif command == 'End':
        substring = args[1]
        if string.endswith(substring):
            print('True')
        else:
            print('False')
    elif command == 'Uppercase':
        string = string.upper()
        print(string)
    elif command == 'FindIndex':
        char = args[1]
        idx = string.find(char)
        if idx >= 0:
            print(idx)
    elif command == 'Cut':
        start_idx = int(args[1])
        length = int(args[2])
        substring = string[start_idx:(start_idx + length)]
        string.replace(substring,'')
        print(string)
