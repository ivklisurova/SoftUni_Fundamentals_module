text = input()

final_string = ''
current_string = ''
repeat = ''

for i in range(len(text)):
    if text[i].isdigit():
        num = text[i]
        counter = i + 1
        while counter < len(text) and text[counter].isdigit():
            num += text[counter]
            counter += 1
        final_string += (current_string.upper() * int(num))
        current_string = ''
    else:
        current_string += text[i]



def unique_ch(string):
    unique_characters = []

    for letter in string:
        if letter not in unique_characters:
            unique_characters.append(letter)

    unique_characters_used = len(unique_characters)
    print(f'Unique symbols used: {unique_characters_used}')


unique_ch(final_string)

print(final_string)
