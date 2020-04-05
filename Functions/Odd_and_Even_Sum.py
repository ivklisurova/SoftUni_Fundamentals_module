number = input()


def odd_or_even(a):
    odd_sum = 0
    even_sum = 0
    for i in a:
        i = int(i)
        if i % 2 != 0:
            odd_sum += i
        elif i % 2 == 0:
            even_sum += i
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


print(odd_or_even(number))