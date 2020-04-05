orders = {}

while True:
    command = input()
    if command == 'buy':
        break
    command = command.split(' ')
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in orders:
        orders[product] = [price, quantity]
    else:
        if orders[product][0] != price:
            orders[product][0] = price
        orders[product][1] += quantity

for k, v in orders.items():
    print(f'{k} -> {(v[0] * v[1]):.2f}')
