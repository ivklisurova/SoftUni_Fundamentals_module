import re

text = input()

threshold_pattern = r'\d'

threshold_match = re.findall(threshold_pattern, text)

result = 0
for i in range(len(threshold_match)):
    if i == 0:
        result = int(threshold_match[i])
    else:
        result *= int(threshold_match[i])

print(f'Cool threshold: {result}')

pattern = r'([*|:]{2})([A-Z][a-z]{2,})(\1)'

matches = re.findall(pattern, text)

print(f'{len(matches)} emojis found in the text. The cool ones are:')

for i in matches:
    coolness = 0
    emoji_text = i[1]
    for x in range(len(emoji_text)) :
        coolness += ord(emoji_text[x])

    if coolness > result:
        print(f'{i[0]}{i[1]}{i[2]}')
