cards = input()

fouls_cards = cards.split()

a_players = []
b_players = []

is_terminated = False

for i in range(1, 12):
    i = f'A-{str(i)}'
    a_players.append(i)
for j in range(1, 12):
    j = f'B-{str(j)}'
    b_players.append(j)

for card in fouls_cards:
    if card in a_players:
        a_players.remove(card)
    elif card in b_players:
        b_players.remove(card)
    else:
        continue
    if len(a_players) == 6 or len(b_players) == 6:
        is_terminated = True
        break

print(f'Team A - {len(a_players)}; Team B - {len(b_players)}')

if is_terminated:
    print('Game was terminated')
