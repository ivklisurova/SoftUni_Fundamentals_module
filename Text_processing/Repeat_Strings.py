string_input = input().split()
result = ''

for word in string_input:
    result += (word * len(word))

print(result)

