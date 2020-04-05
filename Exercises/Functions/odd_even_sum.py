def odd_sum(num):
    result = [int(i) for i in num if int(i) % 2 != 0]
    sum_numbers = sum(result)
    return sum_numbers


def even_sum(num):
    result = [int(i) for i in num if int(i) % 2 == 0]
    sum_numbers = sum(result)
    return sum_numbers


def solve(num):
    result = f'Odd sum = {odd_sum(num)}, Even sum = {even_sum(num)}'
    return result


number = input()

print(solve(number))
