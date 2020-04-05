import re

while True:
    message = input()

    pattern = r'([#|$|%|*|&])([a-zA-Z]+)\1[=]([\d]+)[!]{2}(.+)'

    match = re.findall(pattern, message)

    if len(match) == 0:
        print('Nothing found!')
    else:
        i = match[0]
        racer = i[1]
        length = int(i[2])
        geohash = i[3]

        if len(geohash) == length:
            decrypted_message = ''
            for i in geohash:
                decrypted_message += chr(ord(i) + length)
            print(f'Coordinates found! {racer} -> {decrypted_message}')
            break
        else:
            print('Nothing found!')
