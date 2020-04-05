contacts = input().split(' ')

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Add':
        contact = tokens[1]
        index = int(tokens[2])
        if contact not in contacts:
            contacts.append(contact)
        elif contact in contacts:
            if 0 <= index < len(contacts):
                contacts.insert(index, contact)
    elif command == 'Remove':
        index = int(tokens[1])
        if 0 <= index <= len(contacts):
            contacts.pop(index)
    elif command == 'Export':
        start_idx = int(tokens[1])
        count = int(tokens[2])
        if 0 <= start_idx < len(contacts):
            if 0 <= start_idx+count < len(contacts):
                for i in range(start_idx, start_idx + count):
                    print(contacts[i], end=' ')
            else:
                for i in contacts[start_idx:]:
                    print(i, end=' ')

    elif command == 'Print':
        to_print = tokens[1]
        print('Contacts:', end=' ')
        if to_print == 'Normal':
            [print(x, end=' ') for x in contacts]
            break
        elif to_print == 'Reversed':
            [print(x, end=' ') for x in contacts[::-1]]
            break
