import re

text = input()

pattern = r'\b([_])([a-zA-Z]+|[0-9]+)\b'

match = re.findall(pattern, text)
for i in range(len(match)):
    if i == len(match)-1:
        print(match[i][1])
        break
    print(match[i][1], end=',')
