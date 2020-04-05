def solve(message):
    result = ''
    for ch in message:
        decrypted = ord(ch) + 3
        result += chr(decrypted)

    print(result)


solve(input())
