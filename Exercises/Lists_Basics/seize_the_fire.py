fire_cells = input().split('#')
water = int(input())

HIGH = range(81, 126)
MEDIUM = range(51, 81)
LOW = range(1, 51)

cells_down = []
effort = 0

for i in fire_cells:
    tokens = i.split(' =')
    type_fire = tokens[0]
    value_cell = int(tokens[1])
    if type_fire == 'High':
        if value_cell not in HIGH:
            continue
    elif type_fire == 'Medium':
        if value_cell not in MEDIUM:
            continue
    elif type_fire == 'Low':
        if value_cell not in LOW:
            continue
    if water >= value_cell:
        water -= value_cell
        cells_down.append(value_cell)
        effort += value_cell * 0.25
    elif water < value_cell:
        continue
print('Cells:')

[print(f'- {i}') for i in cells_down]
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells_down)}')
