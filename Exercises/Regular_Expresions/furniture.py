import re

furniture = []
total_money = 0

while True:
    order = input()
    if order == 'Purchase':
        break

    pattern = r'>{2}([a-zA-z]+)<{2}(\d+[.]\d+|\d+)!(\d+)'
    matches = re.findall(pattern, order)

    for i in matches:
        if len(i) == 0:
            break
        furniture.append(i[0])
        total_money += float(i[1]) * float(i[2])

print('Bought furniture:')
[print(x) for x in furniture]

print(f'Total money spend: {total_money:.2f}')
