def is_perfect(num):
    divisors = []
    for i in range(1,num):
        if num % i == 0:
            divisors.append(i)

    if sum(map(int, divisors)) == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


number = int(input())

is_perfect(number)
