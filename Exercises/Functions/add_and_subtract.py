def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)


x = int(input())
y = int(input())
z = int(input())

print(add_and_subtract(x, y, z))
