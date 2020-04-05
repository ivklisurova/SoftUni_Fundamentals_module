def solve(string):
    result = ''
    previous_letter = ''

    for i in string:
        if i != previous_letter:
            result += i
            previous_letter = i

    print(result)


solve(input())
