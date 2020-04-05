text = input()

result = ''
strength = 0

for i, j in enumerate(text):
    if j == '>':
        remove_symbols = int(text[i + 1])
        strength += remove_symbols
        result += j
        continue
    if strength > 0:
        strength -= 1
        continue
    result += j

print(result)
