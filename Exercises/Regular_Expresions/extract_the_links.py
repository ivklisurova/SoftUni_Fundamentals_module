import re

pattern = r'(www)[.]([a-zA-Z0-9]+([\-]*[a-zA-Z0-9]+)*)(([.]([a-z]+)){1,})'

while True:
    text = input()
    if not text:
        break

    match = re.findall(pattern, text)

    result = ''
    for i in match:
        for j,k in enumerate(i):
            if j == 0 or j == 3:
                result += k
            elif j == 1:
                result += '.' + k

    print(result)