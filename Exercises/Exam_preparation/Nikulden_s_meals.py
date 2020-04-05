meals_log = {}

count_unliked_meals = 0

while True:
    tokens = input().split('-')
    command = tokens[0]
    if command == 'Stop':
        break
    guest = tokens[1]
    meal = tokens[2]
    if command == 'Like':
        if guest not in meals_log:
            meals_log[guest] = []
            meals_log[guest].append(meal)
        else:
            if meal not in meals_log[guest]:
                meals_log[guest].append(meal)

    elif command == 'Unlike':
        if guest in meals_log:
            if meal not in meals_log[guest]:
                print(f'{guest} doesn\'t have the {meal} in his/her collection.')
            else:
                meals_log[guest].remove(meal)
                count_unliked_meals+=1
                print(f'{guest} doesn\'t like the {meal}.')
        else:
            print(f'{guest} is not at the party.')

sorted_meal_log = dict(sorted(meals_log.items(), key=lambda x: (-len(x[1]),x[0])))

for k,v in sorted_meal_log.items():
    print(f'{k}: {", ".join(v)}')

print(f'Unliked meals: {count_unliked_meals}')

