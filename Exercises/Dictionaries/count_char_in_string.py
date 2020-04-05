text = input()

occurences = {}

for i in text:
    if i != ' ':
        if i not in occurences:
            occurences[i] = 0
        occurences[i] += 1

[print(f'{k} -> {v}') for k, v in occurences.items()]
