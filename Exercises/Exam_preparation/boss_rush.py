import re

n = int(input())

for i in range(n):
    boss = input()

    pattern = r'[|]([A-Z]{4,})[|][:][#]([a-zA-Z]+[ ][a-zA-Z]+)[#]'

    matches = re.findall(pattern, boss)

    if len(matches) > 0:
        for i in matches:
            print(f'{i[0]}, The {i[1]}')
            print(f'>> Strength: {len(i[0])}')
            print(f'>> Armour: {len(i[1])}')
    else:
        print('Access denied!')
