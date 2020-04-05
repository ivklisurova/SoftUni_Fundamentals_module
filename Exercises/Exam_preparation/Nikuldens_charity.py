text = input()

while True:
    tokens = input().split(' ')
    if tokens[0] == 'Finish':
        break
    command = tokens[0]
    if command == 'Replace':
        current_char = tokens[1]
        new_char = tokens[2]
        text = text.replace(current_char, new_char)
        print(text)
    elif command == 'Cut':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        if start_index >= 0 and end_index < len(text):
            part = text[start_index:end_index + 1]
            text = text.replace(part, '')
            print(text)
        else:
            print('Invalid indexes!')
    elif command == 'Make':
        case = tokens[1]
        if case == 'Upper':
            text = text.upper()
        elif case == 'Lower':
            text = text.lower()
        print(text)
    elif command == 'Check':
        string = tokens[1]
        if string in text:
            print(f'Message contains {string}')
        else:
            print(f'Message doesn\'t contain {string}')
    elif command == 'Sum':
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        substring = text[start_index:end_index + 1]
        sum_substring = 0
        if start_index >= 0 and end_index < len(text):
            for i in substring:
                sum_substring += ord(i)
            print(sum_substring)
        else:
            print('Invalid indexes!')

