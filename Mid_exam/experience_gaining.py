battle_experience = float(input())
battles = int(input())

total_experience = 0
finished_battles = 0

for i in range(1, battles + 1):
    earned_experience = float(input())

    if i % 3 == 0:
        earned_experience += earned_experience * 0.15
    elif i % 5 == 0:
        earned_experience -= earned_experience * 0.10

    total_experience += earned_experience
    finished_battles += 1

    if total_experience >= battle_experience:
        break

if total_experience >= battle_experience:
    print(f'Player successfully collected his needed experience for {finished_battles} battles.')
else:
    print(
        f'Player was not able to collect the needed experience, {battle_experience - total_experience:.2f} more needed.')
