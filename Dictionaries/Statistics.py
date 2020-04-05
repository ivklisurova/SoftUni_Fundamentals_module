products = {}

while True:
    command = input()
    if command == 'statistics':
        break
    else:
        tokens = command.split(': ')
        product = tokens[0]
        quantity = int(tokens[1])

        if product not in products:
            products[product] = 0

        products[product] += quantity

print('Products in stock:')

[print(f'- {product}: {quantity}') for product, quantity in products.items()]


print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')
