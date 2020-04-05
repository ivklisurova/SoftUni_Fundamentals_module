message = input()

encrypted_message = ''

for i in message:
    encrypted_message += chr(ord(i)+3)

print(encrypted_message)

