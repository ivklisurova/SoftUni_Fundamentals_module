def solve(ll, ll_2, a):
    for i in ll:
        if i <= a:
            ll_2.append(i)
    for j in ll_2:
        ll.remove(j)


numbers = list(map(int, input().split(', ')))

boundary = 10

temp_list = []

while True:
    if len(numbers) == 0:
        break
    solve(numbers, temp_list, boundary)
    print(f'Group of {boundary}\'s: {temp_list}')
    temp_list.clear()
    boundary += 10
