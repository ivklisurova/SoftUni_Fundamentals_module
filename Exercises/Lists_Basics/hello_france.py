collection = input().split('|')
budget = float(input())

CLOTHES = 50.00
SHOES = 35.00
ACCESSORIES = 20.50
TICKET_TO_FRANCE = 150

new_collection = []
profit = []

for i in collection:
    tokens = i.split('->')
    item = tokens[0]
    price = float(tokens[1])
    if item == 'Clothes':
        if price > CLOTHES:
            continue
    elif item == 'Shoes':
        if price > SHOES:
            continue
    elif item == 'Accessories':
        if price > ACCESSORIES:
            continue
    if budget >= price:
        budget -= price
        new_collection.append(f'{(price * 1.4):.2f}')
        profit.append(price * 0.4)

total_sum = 0

for i in profit:
    total_sum += float(i)

a = 0
for j in new_collection:
    a += float(j)

[print(i, end=' ') for i in new_collection]

print(f'\nProfit: {total_sum:.2f}')

earnings = a + budget

if earnings >= TICKET_TO_FRANCE:
    print('Hello, France!')
else:
    print('Time to go.')
