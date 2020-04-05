def char_position(letter):
    return ord(letter) - 96


text = input().split()

result = 0

for i in text:
    number = int(i[1:len(i)-1])
    if i[0].isupper():
        result += number / char_position(i[0].lower())
    elif i[0].islower():
        result += number * char_position(i[0].lower())
    if i[-1].isupper():
        result -= char_position(i[-1].lower())
    elif i[-1].islower():
        result += char_position(i[-1].lower())

print(f'{result:.2f}')
