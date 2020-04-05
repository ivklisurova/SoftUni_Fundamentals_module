numbers = input().split()
message = list(input())

indices = []
output = []

for i in numbers:
    sum_num = sum([int(j) for j in i])
    indices.append(sum_num)

for i in indices:
    counter = 0
    while counter != i:
        for k, x in enumerate(message):
            if counter == i:
                output.append(message[k])
                message.pop(k)
                break
            counter += 1

print(''.join(output))
