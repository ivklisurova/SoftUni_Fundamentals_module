import re

n = int(input())

pattern = r'^([$][A-Z][a-z]{2,}[$][:][ ])([\[][0-9]+[]])[|]([\[][0-9]+[]])[|]([\[][0-9]+[]])[|]$|^([%][A-Z][a-z]{2,' \
          r'}[%][:][ ])([\[][0-9]+[]])[|]([\[][0-9]+[]])[|]([\[][0-9]+[]])[|]$'

for _ in range(n):
    text = input()

    match = re.findall(pattern, text)
    list_match = []

    if len(match) > 0:
        for i in match:
            for j in i:
                if j != '':
                    list_match.append(j)
    else:
        print('Valid message not found!')
        continue

    tag = list_match[0].strip('$ % : ')
    first_letter = chr(int(list_match[1].strip('[ ]')))
    second_letter = chr(int(list_match[2].strip('[ ]')))
    third_letter = chr(int(list_match[3].strip('[ ]')))
    print(f'{tag}: {first_letter}{second_letter}{third_letter}')


