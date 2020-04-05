import re

text = input()

pattern = r'(\b(?<=\s)[a-zA-Z0-9]+[.|\-|_]*[a-zA-Z0-9]+@)((?<=@)[a-zA-Z]+[-]*[a-z]*[.][a-zA-Z]+[.][a-zA-Z]+|' \
          r'(?<=@)[a-zA-Z]+[-]*[a-z]*[.][a-zA-Z]+)'

matches = re.findall(pattern, text)

[print(''.join(i)) for i in matches]
