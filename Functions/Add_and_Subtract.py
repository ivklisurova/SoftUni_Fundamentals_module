num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    result = sum_numbers(a,b)
    return subtract(result, c)


print(add_and_subtract(num_1, num_2, num_3))
