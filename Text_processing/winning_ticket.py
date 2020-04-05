tickets = input().split(', ')

for i in tickets:
    if len(i) == 20:
        left_half = i[:10]
        right_half = i[10:]
        for j in range(len(left_half)):
            counter = 0
            if left_half[j] == '@' or left_half[j] == '#' or left_half[j] == '$' or left_half[j] == '^':
                pass






    else:
        print('invalid ticket')
