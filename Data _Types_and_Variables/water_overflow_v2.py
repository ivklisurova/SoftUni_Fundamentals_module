n = int(input())

capacity = 255
water_in_tank = 0

for i in range(n):
    water = int(input())
    if water <= capacity:
        capacity -= water
        water_in_tank += water
    else:
        print('Insufficient capacity!')

print(water_in_tank)



