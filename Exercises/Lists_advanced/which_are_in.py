substrings = input().split(', ')
strings = input().split(', ')

result = []

for i in substrings:
    for j in strings:
        if i in j:
            if i not in result:
                result.append(i)
print(result)