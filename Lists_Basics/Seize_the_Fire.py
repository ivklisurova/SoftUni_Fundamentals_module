fires_cells = input()
watter = int(input())

list_fire = fires_cells.split('#')

water_left = watter
total_fire = 0
effort = 0

print('Cells:')

for i in list_fire:
    idx_fire = i.split('=')
    fire = idx_fire[0]
    range_fire = int(idx_fire[1])
    if water_left < range_fire:
        continue
    if fire == 'High ':
        if 81 <= range_fire <= 125:
            water_left -= range_fire
            effort += range_fire * 0.25
            total_fire += range_fire
        else:
            continue
    elif fire == 'Medium ':
        if 51 <= range_fire <= 80:
            water_left -= range_fire
            effort += range_fire * 0.25
            total_fire += range_fire
        else:
            continue
    elif fire == 'Low ':
        if 1 <= range_fire <= 50:
            water_left -= range_fire
            effort += range_fire * 0.25
            total_fire += range_fire
        else:
            continue
    print(f' - {range_fire}')

print(f'Effort: {effort:.2f}\nTotal Fire: {total_fire}')
