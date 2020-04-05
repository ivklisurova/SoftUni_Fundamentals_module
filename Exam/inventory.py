collection = input().split(', ')

while True:
    tokens = input().split(' - ')
    command = tokens[0]
    if command == 'Craft!':
        print(', '.join(collection))
        break
    elif command == 'Collect':
        item = tokens[1]
        if item not in collection:
            collection.append(item)
    elif command == 'Drop':
        item = tokens[1]
        if item in collection:
            collection.remove(item)
    elif command == 'Combine Items':
        args = tokens[1].split(':')
        old_item = args[0]
        new_item = args[1]
        if old_item in collection:
            for i in range(len(collection)):
                if collection[i] == old_item:
                    collection.insert(i + 1, new_item)
    elif command == 'Renew':
        item = tokens[1]
        for i in range(len(collection)):
            if collection[i] == item:
                collection.pop(i)
                collection.append(item)


