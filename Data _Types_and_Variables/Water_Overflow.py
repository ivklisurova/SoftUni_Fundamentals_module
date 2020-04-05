n = int(input())

free_space = 255
liters_in_tank = 0

for line in range(0, n):
    liters = int(input())
    if liters <= free_space:
        free_space -= liters
        liters_in_tank += liters
    else:
        print('Insufficient capacity!')
        continue

print(liters_in_tank)

