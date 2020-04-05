from collections import Counter

animals = []

while True:
    input_com = input().split(':')
    command = input_com[0]

    if command == 'Last Info':
        break

    name = input_com[1]
    food = int(input_com[2])
    area = input_com[3]

    if command == 'Add':
        if len(animals) == 0:
            new_list = [name, [food, area]]
            animals.append(new_list)
        else:
            for i in animals:
                if i[0] == name:
                    i[1][0] += food
                    break
            else:
                new_list = [name, [food, area]]
                animals.append(new_list)

    elif command == 'Feed':
        for i in animals:
            if i[0] == name:
                i[1][0] -= food
                if i[1][0] <= 0:
                    print(f'{name} was successfully fed')
                    animals.remove(i)

animals.sort(reverse=True)

print('Animals:')

for i in animals:
    print(f'{i[0]} -> {i[1][0]}g')

print('Areas with hungry animals:')

hungry_animals = []
for i in animals:
    hungry_animals.append(i[1][1])

previous_hungry_animal = None
for j in hungry_animals:
    if previous_hungry_animal != j:
        print(f'{j} : {hungry_animals.count(j)}')
        previous_hungry_animal = j


