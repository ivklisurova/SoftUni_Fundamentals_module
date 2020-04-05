treasure_chest = input().split('|')

while True:
    action = input()
    if action == 'Yohoho!':
        break
    split_action = action.split()
    command = split_action[0]
    if command == 'Loot':
        [treasure_chest.insert(0, x) for x in split_action[1::] if x not in treasure_chest]
    elif command == 'Drop':
        idx = int(split_action[1])
        try:
            removed_element = treasure_chest.pop(idx)
            treasure_chest.append(removed_element)
        except IndexError:
            continue
    elif command == 'Steal':
        last_elements = (int(split_action[1]))*-1
        to_be_removed_items = treasure_chest[last_elements:]
        [treasure_chest.remove(x) for x in to_be_removed_items]
        print(', '.join(to_be_removed_items))


a = sum(len(i) for i in treasure_chest)
length_list = len(treasure_chest)

if length_list>0:
    average = f'{(a/length_list):.2f}'
    print(f'Average treasure gain: {average} pirate credits.')
else:
    print('Failed treasure hunt.')


