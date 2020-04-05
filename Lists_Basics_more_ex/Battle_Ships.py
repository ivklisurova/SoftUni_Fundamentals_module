n = int(input())

battle_field = []

for i in range(n):
    row = input()
    list_row = list(map(int, row.split()))
    battle_field.append(list_row)

attacks = input()

attacks_list = attacks.split()

destroyed_ships = 0

for j in attacks_list:
    attack_position = list(map(int, j.split('-')))
    attacked_row = attack_position[0]
    position = attack_position[1]

    for ind, k in enumerate(battle_field[attacked_row]):
        if ind == position:
            if k != 0:
                k -= 1
                battle_field[attacked_row][ind] = k
                if k == 0:
                    destroyed_ships += 1

print(destroyed_ships)
