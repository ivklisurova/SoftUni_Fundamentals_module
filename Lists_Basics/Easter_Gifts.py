names_of_the_gifts = input()

gift_list = names_of_the_gifts.split()

command = input()

while command != 'No Money':

    input_command_list = command.split()
    gift = input_command_list[1]

    if 'OutOfStock' in input_command_list:
        for i in range(len(gift_list)):
            gift_from_current_list = gift_list[i]
            if gift_from_current_list == gift:
                gift_list[i] = 'None'

    elif 'Required' in input_command_list:
        idx = int(input_command_list[2])
        if len(gift_list) > idx:
            gift_list[idx] = gift

    elif 'JustInCase' in input_command_list:
        gift_list[-1] = gift

    command = input()

for k in range(len(gift_list)):
    to_buy = gift_list[k]
    if to_buy != 'None':
        print(to_buy, end=' ')
