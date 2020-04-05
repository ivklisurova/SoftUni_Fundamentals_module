string = input().split()
string_one = string[0]
string_two = string[1]

result = 0

for i in range(max(len(string_one), len(string_two))):
    if len(string_one) > i and len(string_two) > i:
        result += ord(string_one[i]) * ord(string_two[i])
    else:
        if string_one >= string_one:
            result += ord(string_one[i])
        elif string_two >= string_one:
            result += ord(string_two[i])

print(result)
