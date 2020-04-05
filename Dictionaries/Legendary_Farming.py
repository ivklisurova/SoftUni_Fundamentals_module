legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}

winner = ''

while winner == '':
    items = input().lower().split()
    n = len(items)

    for i in range(0, n, 2):
        material = items[i + 1]
        quantity = int(items[i])

        if material in legendary_items:
            legendary_items[material] += quantity
            if legendary_items[material] >= 250:
                winner = material
                legendary_items[material] -= 250
                break
        else:
            if material not in junk_items:
                junk_items[material] = 0
            junk_items[material] += quantity

if winner == 'shards':
    print('Shadowmourne obtained!')
elif winner == 'fragments':
    print('Valanyr obtained!')
elif winner == 'motes':
    print('Dragonwrath obtained!')

legendary_items = dict(sorted(legendary_items.items(), key=lambda x: (-x[1], x[0])))
junk_items = dict(sorted(junk_items.items(), key=lambda x: x[0]))

for k, v in legendary_items.items():
    print(f'{k}: {v}')

for key, value in junk_items.items():
    print(f'{key}: {value}')
