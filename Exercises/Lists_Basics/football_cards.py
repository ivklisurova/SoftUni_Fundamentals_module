team_a = [1]*11
team_b = [1]*11

cards = input().split()
team_a_counter = 11
team_b_counter = 11
is_terminated = False

for x in cards:
    card = x.split('-')
    team = card[0]
    player = int(card[1])
    if team == 'A':
        if team_a[player - 1] == 0:
            continue
        else:
            team_a[player - 1] = 0
            team_a_counter -= 1

    elif team == 'B':
        if team_b[player - 1] == 0:
            continue
        else:
            team_b[player - 1] = 0
            team_b_counter -= 1

    if team_a_counter < 7 or team_b_counter < 7:
        is_terminated = True
        break

print(f'Team A - {team_a_counter}; Team B - {team_b_counter}')

if is_terminated:
    print('Game was terminated')

