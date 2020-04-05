def int_scenario(num):
    result = int(num) * 2
    return result


def double_scenario(num):
    result = f'{(float(num) * 1.5):.2f}'
    return result


def string_scenario(string):
    result = f'${string}$'
    return result


def solve(a,b):
    if a == 'int':
        return int_scenario(b)
    elif a == 'real':
        return double_scenario(b)
    elif a == 'string':
        return string_scenario(b)


operation = input()
user_input = input()

print(solve(operation,user_input))

