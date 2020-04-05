items = input()
budget = float(input())

TICKET_COST = 130

left_budget = budget

list_items = items.split('|')
list_new_prices = []

for i in list_items:
    type_price_list = i.split('->')
    type_item = type_price_list[0]
    price_item = float(type_price_list[1])

    if left_budget < price_item:
        continue

    if type_item == 'Clothes':
        if price_item <= 50:
            left_budget -= price_item
            new_price = f'{(price_item * 1.4):.2f}'
            list_new_prices.append(new_price)
        else:
            continue
    elif type_item == 'Shoes':
        if price_item <= 35:
            left_budget -= price_item
            new_price = f'{(price_item * 1.4):.2f}'
            list_new_prices.append(new_price)
        else:
            continue
    elif type_item == 'Accessories':
        if price_item <= 20.50:
            left_budget -= price_item
            new_price = f'{(price_item * 1.4):.2f}'
            list_new_prices.append(new_price)
        else:
            continue

money_needed = budget - left_budget
income = sum(list(map(float, list_new_prices)))
profit = income - money_needed
money_for_travel = income + left_budget

print(*list_new_prices)
print(f'Profit: {profit:.2f}')

if money_for_travel >= TICKET_COST:
    print('Hello, France!')
else:
    print('Time to go.')
