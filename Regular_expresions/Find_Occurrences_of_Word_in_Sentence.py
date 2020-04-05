import re

text = input().lower()
word_to_match = input()

pattern = r'\b' + re.escape(word_to_match) + r'\b'


matches = re.findall(pattern, text)
count_matches = len(matches)
print(count_matches)
