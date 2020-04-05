import re

n = int(input())

for i in range(n):
    message = input()

    pattern = r'([*|@])([A-Z][a-z]{2,})\1[:][ ](([\[]([a-zA-Z])[\]][|]){3})$'

    match = re.findall(pattern, message)

    if len(match) > 0:
        result = ''
        for y in match:
            result += y[1] + ': '
            for z in y[2]:
                if z != '[' and z != ']' and z != '|':
                    result += str(ord(z)) + ' '
        print(result)
    else:
        print(f'Valid message not found!')
