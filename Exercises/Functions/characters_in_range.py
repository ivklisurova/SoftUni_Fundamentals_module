def solve(start_char, end_char):
    start = ord(start_char)
    end = ord(end_char)
    result = [chr(i) for i in range(start + 1, end)]
    return result


a = input()
b = input()

print(' '.join(solve(a,b)))
