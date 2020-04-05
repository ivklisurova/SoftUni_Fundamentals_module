n = int(input())

is_prime = False

for item in range(2, n):
    if n % item == 0:
        is_prime = False
        break
    else:
        is_prime = True


print(f'{is_prime}')
