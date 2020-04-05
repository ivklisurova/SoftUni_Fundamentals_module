current_version = list(map(int, input().split('.')))

current_version[2] = current_version[2] + 1

if current_version[2] > 9:
    current_version[1] += 1
    current_version[2] = 0
    if (current_version[1]) > 9:
        current_version[1] = 0
        current_version[0] += 1

print(*current_version, sep='.')
