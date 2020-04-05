import math

count_biscuits = int(input())
count_workers = int(input())
competitive_factory_prod = int(input())

total_production = 0

for day in range(1,31):
    daily_production = count_biscuits * count_workers
    if day % 3 == 0:
        total_production += (math.floor(daily_production*0.75))
    else:
        total_production += daily_production

print(f'You have produced {total_production} biscuits for the past month.')

diff = abs(total_production - competitive_factory_prod)
percentage = (diff/competitive_factory_prod)*100

if total_production >= competitive_factory_prod:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {percentage:.2f} percent less biscuits.')

