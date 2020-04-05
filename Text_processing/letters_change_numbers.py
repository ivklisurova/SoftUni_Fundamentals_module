import string

text = input().split()

alphabet = list(string.ascii_lowercase)

final_result = 0

for i in text:
    result = 0
    first_letter = i[0]
    last_letter = i[-1]
    number = int(i[1:len(i) - 1])
    letter_position_first_letter = (alphabet.index(first_letter.lower())) + 1
    letter_position_last_letter = (alphabet.index(last_letter.lower())) + 1
    if first_letter.isupper():
        result = number / letter_position_first_letter
    elif first_letter.islower():
        result = number * letter_position_first_letter
    if last_letter.isupper():
        result -= letter_position_last_letter
    elif last_letter.islower():
        result += letter_position_last_letter

    final_result += result


print(f'{final_result:.2f}')
