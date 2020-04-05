stores = {}

while True:
    tokens = input().split('->')
    command = tokens[0]
    if command == 'END':
        break
    shop = tokens[1]

    if command == 'Add':
        items = tokens[2].split(',')
        if shop not in stores:
            stores[shop] = []
        if shop in stores:
            stores[shop] += items

    elif command == 'Remove':
        if shop in stores:
            stores.pop(shop)

print('Stores list:')

sorted_stores_log = dict(sorted(stores.items(), key=lambda x: ((len(x[1]),x[0])), reverse=True))

for k in sorted_stores_log:
    print(k)
    for v in sorted_stores_log[k]:
        print(f'<<{v}>>')
