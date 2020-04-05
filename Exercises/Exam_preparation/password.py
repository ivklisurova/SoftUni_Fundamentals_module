import re

n = int(input())

for i in range(n):
    password = input()
    pattern = r'(.+)>(\d{3})[|]([a-z]{3})[|]([A-Z]{3})[|]([^<>]{3})<\1'

    match = re.findall(pattern, password)

    if len(match) > 0:
        for x in match:
            encrypted_password = x[1]+x[2]+x[3]+x[4]
            print(f'Password: {encrypted_password}')
    else:
        print('Try another password!')