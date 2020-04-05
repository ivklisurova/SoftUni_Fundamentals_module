import re

pattern = r'(?P<day>\b\d{2})([.\-\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})'
dates = input()

matches = re.findall(pattern, dates)


for match in matches:
    print(f'Day: {match[0]}, Month: {match[2]}, Year: {match[3]}')