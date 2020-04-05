days_adventure = int(input())
count_players = int(input())
group_energy = float(input())
water = float(input())
food = float(input())

total_water = days_adventure * count_players * water
total_food = days_adventure * count_players * food

for i in range(1, days_adventure + 1):
    chopping_wood_energy = float(input())
    group_energy -= chopping_wood_energy
    if group_energy <= 0:
        print(f'You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.')
        break
    if i % 2 == 0:
        group_energy += group_energy * 0.05
        total_water -= total_water * 0.3
    if i % 3 == 0:
        total_food -= total_food / count_players
        group_energy += group_energy * 0.1

if group_energy > 0:
    print(f'You are ready for the quest. You will be left with - {group_energy:.2f} energy!')
