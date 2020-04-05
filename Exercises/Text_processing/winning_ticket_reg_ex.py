import re

tickets_log = input().split(', ')

pattern = r'\${6,}|\@{6,}|\#{6,}|\^{6,}'

for ticket in tickets_log:
    if len(ticket) < 20 or len(ticket) > 20:
        print('invalid ticket')
    else:
        left_half = ticket[:10]
        right_half = ticket[10:]

        a = re.findall(pattern, left_half)
        b = re.findall(pattern, right_half)
        if len(a) == 0 or len(b) == 0:
            print(f'ticket "{ticket}" - no match')
            continue
        length_a = len(a[0])
        length_b = len(b[0])

        if length_a == length_b:
            if 6 <= length_a <= 9:
                print(f'ticket "{ticket}" - {length_a}{a[0][0]}')
            elif length_a > 9:
                print(f'ticket "{ticket}" - {length_a}{a[0][0]} Jackpot!')
