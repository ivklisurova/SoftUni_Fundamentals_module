string = input()


def palindrome(a):
    list_numbers = string.split(', ')
    is_palindrome = False

    for i in list_numbers:
        x = i[::-1]
        if x == i:
            is_palindrome = True
            print(is_palindrome)
        else:
            is_palindrome = False
            print(is_palindrome)
    return is_palindrome


palindrome(string)
