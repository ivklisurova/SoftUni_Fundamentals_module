divisor = int(input())
bound = int(input())

n = None
is_divided = False

for num in reversed(range(0, bound+1)):
    if num % divisor == 0:
        is_divided = True
        n = num
        break

print(n)