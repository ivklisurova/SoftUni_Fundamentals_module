# def solve(bakery_str):
#     values = bakery_str.split()
#     bakery = {}
#     n = len(values)
#     for i in range(0, n, 2):
#         food = values[i]
#         quantity = int(values[i + 1])
#         bakery[food] = quantity
#     print(bakery)


def solve(bakery_str):
    values = bakery_str.split()
    n = len(values)
    bakery = {values[i]: int(values[i + 1]) for i in range(0,n,2)}
    print(bakery)


solve(input())
