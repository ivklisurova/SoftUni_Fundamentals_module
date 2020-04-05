import re

pattern = r'(\b(?<=>>)[A-z]+)<<((?<=<<)[0-9]+[.][0-9]+)!((?<=!)[0-9]+)\b|(\b(?<=>>)[A-z]+)<<((?<=<<)[0-9]+)!((?<=!)[0-9]+)\b'

total_money = 0
bought_furniture = []


while True:
    token = input()
    if token == 'Purchase':
        break

    matches = re.findall(pattern,token)
    list_matches = []
    for i in matches:
        for j in i:
            if j != '':
                list_matches.append(j)

    if len(list_matches) > 0:
        bought_furniture.append(list_matches[0])
        total_money += (float(list_matches[1]) * int(list_matches[2]))


print('Bought furniture:')
for i in bought_furniture:
    print(i)

print(f'Total money spend: {total_money:.2f}')

