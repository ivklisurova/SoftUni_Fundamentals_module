def repeat_string(s, rep):
    if rep < 1:
        return ''
    return s + repeat_string(s, rep=rep - 1)


input_str = input()
n = int(input())

print(repeat_string(input_str, n))
