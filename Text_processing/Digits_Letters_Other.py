def solve(text):
    digits = ''
    letters = ''
    others = ''

    for ch in text:
        if ch.isdigit():
            digits += ch
        elif ch.isalpha():
            letters += ch
        elif not ch.isalnum():
            others += ch

    print(digits)
    print(letters)
    print(others)


solve(input())


