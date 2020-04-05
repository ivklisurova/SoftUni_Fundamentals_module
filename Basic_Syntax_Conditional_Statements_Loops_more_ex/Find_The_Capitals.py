word = input()

array_ch = []

for position, ch in enumerate(word):
    if 65 <= ord(ch) <= 90:
        array_ch.append(position)


print(array_ch)