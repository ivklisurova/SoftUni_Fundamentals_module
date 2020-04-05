from operator import itemgetter

animals = {}
areas = {}

while True:
    tokens = input().split(':')
    if tokens[0] == 'Last Info':
        break
    action = tokens[0]
    name = tokens[1]
    food = int(tokens[2])
    area = tokens[3]

    if action == 'Add':
        if area not in areas:
            areas[area] = 0
        if name in animals:
            animals[name] += food
        if name not in animals:
            animals[name] = food
            areas[area] += 1

    elif action == 'Feed':
        if name in animals:
            animals[name] -= food
            if animals[name] <= 0:
                print(f'{name} was successfully fed')
                animals.pop(name)
                areas[area] -= 1

sorted_animals = dict(sorted(animals.items(), key=itemgetter(1, 0), reverse=True))
sorted_areas = dict(sorted(areas.items(), key=lambda x: x[0], reverse=True))
print('Animals:')
[print(f'{x} -> {y}g') for x, y in sorted_animals.items()]
print('Areas with hungry animals:')
[print(f'{x} : {y}') for x, y in sorted_areas.items() if y > 0]
