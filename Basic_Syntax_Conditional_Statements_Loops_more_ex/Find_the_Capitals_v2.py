word = input()

capital_letter_idx = []

for idx,letter in enumerate(word):
    if 65 <= ord(letter) <= 90:
        capital_letter_idx.append(idx)

print(capital_letter_idx)
