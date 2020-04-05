import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


def cartesian(a, b, c, d):
    first_point = math.sqrt(math.pow(abs(a), 2) + math.pow(abs(b), 2))
    second_point = math.sqrt(math.pow(abs(c), 2) + math.pow(abs(d), 2))

    if second_point < first_point:
        print(f'({c}, {d})')

    else:
        print(f'({a}, {b})')


cartesian(x1,y1, x2, y2)