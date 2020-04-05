def first_letter(string, temp_list):
    letter = ''
    for x in string:
        if x.isdigit():
            letter += x
    deciphered_letter = chr(int(letter))
    temp_list.append(deciphered_letter)
    return temp_list


def the_rest_of_the_letters(string, temp_list):
    for y in string:
        if y.isalpha():
            temp_list.append(y)
    return temp_list


message = input().split()

deciphered_message = []
for i in message:
    word = []
    first_letter(i, word)
    the_rest_of_the_letters(i, word)

    word[1], word[-1] = word[-1], word[1]

    deciphered_message.append(''.join(word))

print(' '.join(deciphered_message))
