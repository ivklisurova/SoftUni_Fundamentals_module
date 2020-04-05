action = input()
number = input()


def solve(a, b):
    result = None
    if action == 'int':
        b = int(b)
        result = b * 2
    elif action == 'real':
        b = float(b)
        result = f'{(b * 1.5):.2f}'
    elif action == 'string':
        result = f'${b}$'
    return result


print(solve(action, number))
