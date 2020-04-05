key = int(input())
n = int(input())

decrypted_message = []

for i in range(n):
    symbol = input()
    decrypted_symbol = ord(symbol)+key
    decrypted_message.append(chr(decrypted_symbol))

print(''.join(decrypted_message))
