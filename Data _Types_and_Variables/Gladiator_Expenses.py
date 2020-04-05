lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_spent = 0
counter_shield_brakes = 0

for game in range(1, lost_fights_count + 1):
    if game % 2 == 0:
        total_spent += helmet_price
        if game % 3 == 0:
            total_spent += shield_price
            counter_shield_brakes += 1
            if counter_shield_brakes == 2:
                total_spent += armor_price
                counter_shield_brakes = 0
    if game % 3 == 0:
        total_spent += sword_price

print(f'Gladiator expenses: {total_spent:.2f} aureus')
