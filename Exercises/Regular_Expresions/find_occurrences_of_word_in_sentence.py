import re

text = input().lower()
word = input().lower()

pattern = r'\b' + re.escape(word) + r'\b'

match = re.findall(pattern, text)
occurrences = len(match)
print(occurrences)
