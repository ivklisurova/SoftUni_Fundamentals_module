def solve(products_quantity_str, search_str):
    values = products_quantity_str.split()
    n = len(values)
    stock_dict = {values[i]: int(values[i + 1]) for i in range(0, n, 2)}

    for product in search_str.split():
        if product in stock_dict:
            print(f'We have {stock_dict[product]} of {product} left')
        else:
            print(f'Sorry, we don\'t have {product}')


solve(input(),input())
