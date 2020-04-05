numbers = input()
beggar_count = int(input())

amount = numbers.split(', ')
beggars_amount = []

for beggar in range(beggar_count):
    beggar_sum = 0
    for number in range(beggar, len(amount), beggar_count):
        number = int(amount[number])
        beggar_sum += number

    beggars_amount.append(beggar_sum)

print(beggars_amount)
