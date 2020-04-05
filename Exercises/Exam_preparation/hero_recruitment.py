spellbook = {}

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'End':
        break
    hero_name = tokens[1]

    if command == 'Enroll':
        if hero_name not in spellbook:
            spellbook[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')

    elif command == 'Learn':
        spell_name = tokens[2]
        if hero_name in spellbook:
            if spell_name in spellbook[hero_name]:
                print(f'{hero_name} has already learnt {spell_name}.')
            else:
                spellbook[hero_name].append(spell_name)
        else:
            print(f'{hero_name} doesn\'t exist.')

    elif command == 'Unlearn':
        spell_name = tokens[2]
        if hero_name not in spellbook:
            print(f'{hero_name} doesn\'t exist.')
        else:
            if spell_name not in spellbook[hero_name]:
                print(f'{hero_name} doesn\'t know {spell_name}.')
            else:
                spellbook[hero_name].remove(spell_name)

spellbook_sorted = dict(sorted(spellbook.items(), key=lambda x: [-len(x[1]), x[0]]))

print('Heroes:')

for k, v in spellbook_sorted.items():
    print(f'== {k}: {", ".join(v)}')
