integers_list = input().split(', ')

boundary = 10

while True:
    if len(integers_list) == 0:
        break
    else:
        new_list = []
        for i, num in enumerate(integers_list):
            num = int(num)
            if num <= boundary:
                new_list.append(num)

        for j in new_list:
            integers_list.remove(str(j))

        print(f'Group of {boundary}\'s: {new_list}')

    boundary += 10
