first_n = int(input())
second_n = int(input())
third_n = int(input())


def smallest(a, b, c):
    result = min(a, b, c)
    return result


print(smallest(first_n, second_n, third_n))
