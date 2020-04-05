while True:
    user_input = input()
    if user_input == 'end':
        break
    args = user_input.split(':')
    artist = args[0]
    song = args[1]

    is_valid = False

    is_valid_artist = False
    is_valid_song = False

    artist_validation = False
    if artist[0].isupper() and artist[1:len(artist)].islower():
        is_valid_artist = True
    if song.isupper():
        is_valid_song = True

    if is_valid_song and is_valid_artist:
        is_valid = True

    if is_valid:
        key = len(artist)
        result = ''
        for i in user_input:
            ascii_value = ord(i) + key
            if i.isupper() and ascii_value <= 90:
                result += chr(ascii_value)
            elif i.isupper() and ascii_value > 90:
                result += chr(ascii_value - 26)
            elif i.islower() and ascii_value <= 122:
                result += chr(ascii_value)
            elif i.islower() and ascii_value > 122:
                result += chr(ascii_value - 26)
            elif i == ':':
                result += '@'
            elif i == ' ' or i == "'":
                result += i

        print(f'Successful encryption: {result}')
    else:
        print('Invalid input!')

