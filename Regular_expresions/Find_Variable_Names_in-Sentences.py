import re

pattern = r'\b(_{1})([A-Za-z]+|[0-9]+)\b'

text = input()

matches = re.findall(pattern,text)

len_matches = len(matches)

for rot, match in enumerate(matches):
    if rot == len(matches)-1:
        print(match[1])
    else:
        print(match[1], end=',')
