text = input()

final_result = ''
result = ''
unique_symbols = []

for n, i in enumerate(text):
    if i.isalpha():
        result += i.upper()
    elif not i.isalnum():
        result += i
    if i.isdigit():
        multiplier = ''
        for x in range(n,len(text)):
            if text[x].isdigit():
                multiplier += text[x]
            else:
                break
        final_result += result * int(multiplier)
        result = ''

for i in final_result:
    if i not in unique_symbols:
        unique_symbols.append(i)

print(f'Unique symbols used: {len(unique_symbols)}')
print(final_result)
