import re

sentence = input()
sentence_words = re.findall(r"\b[a-zA-z']+\b", sentence)
word = input().lower()
counter = 0

for i in sentence_words:
    i = i.lower()
    if i == word:
        counter += 1

print(counter)