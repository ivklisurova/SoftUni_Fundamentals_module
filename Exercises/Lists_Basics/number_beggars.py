loot = input().split(', ')
beggar_count = int(input())

beggars_loot = []

for beggar in range(beggar_count):
    beggar_sum = 0
    for number in range(beggar, len(loot), beggar_count):
        number = int(loot[number])
        beggar_sum += number

    beggars_loot.append(beggar_sum)

print(beggars_loot)