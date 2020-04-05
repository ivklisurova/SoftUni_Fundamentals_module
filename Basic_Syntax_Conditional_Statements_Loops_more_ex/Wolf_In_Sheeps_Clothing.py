queue = input()

animals = queue.split(', ')
ship_counter = 0

for position, animal in enumerate(reversed(animals)):
    if position == 0 and animal == 'wolf':
        print('Please go away and stop eating my sheep')
        break
    elif position != 0 and animal == 'wolf':
        print(f'Oi! Sheep number {ship_counter}! You are about to be eaten by a wolf!')
        break
    else:
        ship_counter += 1
