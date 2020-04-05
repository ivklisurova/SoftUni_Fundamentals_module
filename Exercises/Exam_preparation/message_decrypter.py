import re

n = int(input())

for i in range(n):
    message = input()

    pattern = r'^([$|%])([A-Z][a-z]{2,})\1[:][ ]([\[]([\d]+)[\]][|])([\[]([\d]+)[\]][|])([\[]([\d]+)[\]][|])$'
    match = re.findall(pattern, message)

    if len(match) > 0:
        for x in match:
            result = chr(int(x[3])) + chr(int(x[5])) + chr(int(x[7]))
            print(f'{x[1]}: {result}')
    else:
        print(f'Valid message not found!')
