given_string = input()

str_dict = {}

for letter in given_string:
    if letter == ' ':
        continue
    if letter not in str_dict:
        str_dict[letter] = 0
    str_dict[letter] += 1

[print(f'{key} -> {value}') for key, value in str_dict.items()]
# for key,value in str_dict.items():
#     print(f'{key} -> {value}')
