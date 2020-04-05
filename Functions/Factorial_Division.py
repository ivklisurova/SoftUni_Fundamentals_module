import numpy

num_1 = int(input())
num_2 = int(input())


def factorial(a, b):
    list_a = list(range(1, num_1 + 1))
    list_b = list(range(1, num_2 + 1))

    result_1 = numpy.prod(list_a)
    result_2 = numpy.prod(list_b)

    final_result = result_1 / result_2
    return f'{final_result:.2f}'


print(factorial(num_1, num_2))
