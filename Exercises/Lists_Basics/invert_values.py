numbers = input().split()

opposite_numbers =[]

for i in numbers:
    num = int(i) * -1
    opposite_numbers.append(num)

print(opposite_numbers)

