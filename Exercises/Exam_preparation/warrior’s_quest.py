text = input()

while True:
    tokens = input()
    if tokens == 'For Azeroth':
        break
    tokens = tokens.split(' ')
    command = tokens[0]
    if command == 'GladiatorStance':
        text = text.upper()
        print(text)
    elif command == 'DefensiveStance':
        text = text.lower()
        print(text)
    elif command == 'Dispel':
        index = int(tokens[1])
        letter = tokens[2]
        text = list(text)
        if 0 <= index < len(text):
            text[index] = letter
            print('Success!')
        else:
            print('Dispel too weak.')
        text = ''.join([str(elem) for elem in text])
    elif command == 'Target':
        substring = tokens[2]
        if tokens[1] == 'Change':
            second_substring = tokens[3]
            if substring in text:
                text = text.replace(substring, second_substring)
                print(text)
        elif tokens[1] == 'Remove':
            if substring in text:
                text = text.replace(substring, '')
            print(text)
    else:
        print('Command doesn\'t exist!')
