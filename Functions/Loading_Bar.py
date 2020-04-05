number = int(input())


def loading(num):
    loading_bar = []
    x = num // 10
    y = ((100 - num) // 10)
    z = '[' + x * '%' + y * '.' + ']'
    loading_bar.append(z)
    if (number // 10) == 10:
        loading_bar.insert(0, '100% Complete!')
        print(loading_bar[0])
        print(loading_bar[1])
    else:
        loading_bar.insert(0, f'{num}%')
        loading_bar.append('Still loading...')
        print(' ' .join(loading_bar[0:2]))
        print(loading_bar[2])
    return loading_bar


loading(number)

