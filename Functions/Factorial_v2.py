num_1 = int(input())
num_2 = int(input())


def factorial(a, b):
    list_a = list(range(1, num_1 + 1))
    list_b = list(range(1, num_2 + 1))

    result = 1
    for i in list_a:
        result = result * i

    result_2 = 1
    for j in list_b:
        result_2 = result_2 * j

    final_result = f'{(result / result_2):.2f}'

    return final_result


print(factorial(num_1, num_2))
