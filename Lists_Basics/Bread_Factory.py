n = input()

list_activities = n.split('|')

energy = 100
coins = 100
counter_act = 0

for activity in list_activities:
    task_list = activity.split('-')
    task = task_list[0]
    num = int(task_list[1])
    counter_act += 1

    if task == 'rest':
        sum_energy = energy + num
        if sum_energy >= 100:
            print('You gained 0 energy.')
        else:
            energy += num
            print(f'You gained {num} energy.')
        print(f'Current energy: {energy}.')
    elif task == 'order':
        if energy >= 30:
            energy -= 30
            coins += num
            print(f'You earned {num} coins.')
        else:
            print('You had to rest!')
            energy += 50
            continue
    else:
        if coins >= num:
            coins -= num
            print(f'You bought {task}.')
        else:
            print(f'Closed! Cannot afford {task}.')
            break


if counter_act == int(len(list_activities)):
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')