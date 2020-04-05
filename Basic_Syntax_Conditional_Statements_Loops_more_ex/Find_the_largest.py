number = input()

list_numbers = []

for i in number:
    i = int(i)
    list_numbers.append(i)

list_numbers.sort(reverse=True)

print(*list_numbers, sep='')
