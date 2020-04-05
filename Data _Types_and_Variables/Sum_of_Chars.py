n = int(input())

ascii_sum = 0

for item in range(n):
    symbol = input()
    ascii_sum += ord(symbol)

print(f'The sum equals: {ascii_sum}')
