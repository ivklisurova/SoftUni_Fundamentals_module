def factorial(a):
    result = 1
    row = [int(x) for x in range(1, a)]
    for i in row:
        result += (result * i)
    return result


def solve(b, c):
    result = f'{(factorial(b) / factorial(c)):.2f}'
    return result


first_num = int(input())
second_num = int(input())

print(solve(first_num, second_num))
