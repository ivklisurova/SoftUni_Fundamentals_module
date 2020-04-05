password = input()


def is_valid(string):
    valid_length = False
    only_letters_and_digits = False
    at_least_two_digits = False

    if 6 <= len(password) <= 10:
        valid_length = True
    else:
        valid_length = False
        print('Password must be between 6 and 10 characters')

    for i in password:
        if 48 <= ord(i) <= 57:
            only_letters_and_digits = True
        elif 65 <= ord(i) <= 90:
            only_letters_and_digits = True
        elif 97 <= ord(i) <= 122:
            only_letters_and_digits = True
        else:
            only_letters_and_digits = False
            print('Password must consist only of letters and digits')
            break

    counter_digits = 0

    for i in password:
        if 48 <= ord(i) <= 57:
            counter_digits += 1

    if counter_digits >= 2:
        at_least_two_digits = True
    else:
        print(f'Password must have at least 2 digits')
        at_least_two_digits= False

    if valid_length and at_least_two_digits and only_letters_and_digits:
        print('Password is valid')


is_valid(password)