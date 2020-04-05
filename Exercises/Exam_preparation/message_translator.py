import re

n = int(input())

for i in range(n):
    message = input()

    pattern = r'!([A-Z][a-z]{2,})!:[\[]([a-zA-z]{8,})[\]]'

    match = re.findall(pattern, message)

    if len(match) > 0:
        result = []
        for j in match:
            command = j[0]
            current_message = j[1]
            for letter in current_message:
                result.append(str(ord(letter)))
            print(f'{command}: {" ".join(result)}')
    else:
        print('The message is invalid')
