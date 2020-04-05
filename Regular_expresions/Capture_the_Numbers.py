import re

pattern = r'\d+'

while True:
    text = input()
    if not text:
        break

    matches = re.findall(pattern,text)

    for i in matches:
        print(i, end=' ')