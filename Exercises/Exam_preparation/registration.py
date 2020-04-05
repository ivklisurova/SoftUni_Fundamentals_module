import re

n = int(input())
successful_registrations = 0

for i in range(n):
    registration = input()

    pattern = r'U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}[0-9]+)P@\$'

    matches = re.findall(pattern, registration)

    if len(matches) > 0:
        successful_registrations += 1
        print('Registration was successful')
        for x in matches:
            print(f'Username: {x[0]}, Password: {x[1]}')
    else:
        print('Invalid username or password')

print(f'Successful registrations: {successful_registrations}')
