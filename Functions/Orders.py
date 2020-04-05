product = input()
quantity = int(input())


def total_price(prod, qty):
    total = None
    if prod == 'coffee':
        total = qty * 1.5
    elif prod == 'water':
        total = qty * 1
    elif prod == 'coke':
        total = qty * 1.4
    elif prod == 'snacks':
        total = qty * 2.00
    return f'{total:.2f}'


print(total_price(product, quantity))
