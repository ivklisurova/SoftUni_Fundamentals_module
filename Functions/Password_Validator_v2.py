password = input()


def password_validation(pass_string):
    output = []
    valid_length = 6 <= len(pass_string) <= 10
    letters_and_digits_only = pass_string.isalnum()
    at_least_2_digits = len([x for x in pass_string if x.isdigit()]) >= 2

    if valid_length and letters_and_digits_only and at_least_2_digits:
        output.append('Password is valid')
    if not letters_and_digits_only:
        output.append('Password must consist only of letters and digits')
    if not valid_length:
        output.append('Password must be between 6 and 10 characters')
    if not at_least_2_digits:
        output.append('Password must have at least 2 digits')

    return output


print('\n'.join(password_validation(password)))
