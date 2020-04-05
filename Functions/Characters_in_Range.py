first_ch = input()
second_ch = input()


def in_between(a, b):
    result = ''
    for i in range(ord(a) + 1, ord(b)):
        result += chr(i) + ' '

    return result


print(in_between(first_ch,second_ch))
