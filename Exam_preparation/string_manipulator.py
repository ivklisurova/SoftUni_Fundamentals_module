my_string = input()

while True:
    command = input()
    if command == 'End':
        break
    command = command.split()
    if command[0] == 'Translate':
        char = command[1]
        replacement = command[2]
        my_string = my_string.replace(char, replacement)
        print(my_string)
    elif command[0] == 'Includes':
        string = command[1]
        print(string in my_string)
    elif command[0] == 'Start':
        start_string = command[1]
        print(my_string.startswith(start_string))
    elif command[0] == 'Lowercase':
        my_string = my_string.lower()
        print(my_string)
    elif command[0] == 'FindIndex':
        letter = command[1]
        index = None
        for i in range(len(my_string)):
            if my_string[i] == letter:
                index = i
        print(index)
    elif command[0] == 'Remove':
        end = int(command[2])
        print(my_string[end:])
