message = input().split()

deciphered_message = []

for i in message:
    first_letter = ''
    word = ''
    for j in i:
        if j.isalpha():
            word += j
        if j.isdigit():
            first_letter += j

    first_letter = chr(int(first_letter))
    deciphered_word = f'{first_letter}{word}'
    deciphered_message.append(deciphered_word)

for i in deciphered_message:
    i_list = list(i)
    i_list[1], i_list[-1] = i_list [-1], i_list[1]

    print(''.join(i_list), end=' ')
