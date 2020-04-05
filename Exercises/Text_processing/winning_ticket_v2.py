tickets_log = input().split(', ')

for ticket in tickets_log:
    ticket = ticket.strip(' ')
    if len(ticket) < 20 or len(ticket) > 20:

        print('invalid ticket')
    else:
        left_half = ticket[:10]
        right_half = ticket[10:]
        symbol = ''
        first_occurrence = 0
        symbol_counter_left_side = 0
        symbol_counter_right_side = 0

        for i in range(len(left_half)):
            if ticket[i] == '^' or ticket[i] == '$' or ticket[i] == '#' or ticket[i] == '@':
                symbol = ticket[i]
                first_occurrence = i
                break
        for j in left_half[first_occurrence:len(left_half)]:
            if j == symbol:
                symbol_counter_left_side += 1
            else:
                break
        for i in range(len(right_half)):
            if ticket[i] == '^' or ticket[i] == '$' or ticket[i] == '#' or ticket[i] == '@':
                symbol = ticket[i]
                first_occurrence = i
                break
        for j in left_half[first_occurrence:len(right_half)]:
            if j == symbol:
                symbol_counter_right_side += 1
            else:
                break
        if symbol_counter_left_side == symbol_counter_right_side:
            if 6 <= symbol_counter_left_side <= 9:
                print(f'ticket "{ticket}" - {symbol_counter_left_side}{symbol}')
            elif symbol_counter_left_side > 9:
                print(f'ticket "{ticket}" - {symbol_counter_left_side}{symbol} Jackpot!')
            else:
                print(f'ticket "{ticket}" - no match')

