import re

pattern = r'(^|(?<=\s))(-?\d+([.]\d+)?($|(?=\s)))'

text = input()

matches = re.findall(pattern,text)

# for match in matches:
#     print(match[1],end=' ')

[print(match[1],end=' ') for match in matches]