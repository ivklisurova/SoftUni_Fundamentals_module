text = input()

while True:
    args = input().split(' ')
    command = args[0]
    if command == 'End':
        break
    if command == 'Translate':
        char = args[1]
        replacement = args[2]
        text = text.replace(char, replacement)
        print(text)
    elif command == 'Includes':
        substring = args[1]
        if substring in text:
            print('True')
        else:
            print('False')
    elif command == 'Start':
        substring = args[1]
        if text.startswith(substring):
            print('True')
        else:
            print('False')
    elif command == 'Lowercase':
        text = text.lower()
        print(text)
    elif command == 'FindIndex':
        char = args[1]
        idx = text.rfind(char)
        print(idx)
    elif command == 'Remove':
        start_idx = int(args[1])
        count = int(args[2])
        if 0 <= start_idx < len(text):
            sub = text[start_idx:(start_idx + count)]
            text = text.replace(sub, '')
            print(text)
