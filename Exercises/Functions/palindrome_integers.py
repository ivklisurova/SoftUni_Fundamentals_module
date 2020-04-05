def solve_palindrome(number):
    is_palindrome = False
    if number == number[::-1]:
        is_palindrome = True
    return is_palindrome


list_numbers = input().split(', ')

[print(solve_palindrome(i)) for i in list_numbers]
