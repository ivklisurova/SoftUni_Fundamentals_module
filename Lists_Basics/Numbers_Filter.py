n = int(input())

ll_unfiltered = []
ll_filtered = []

for i in range(n):
    current_num = int(input())
    ll_unfiltered.append(current_num)

command = input().lower()

if command == 'even':
    for num in ll_unfiltered:
        if num % 2 == 0:
            ll_filtered.append(num)
elif command == 'odd':
    for num in ll_unfiltered:
        if num % 2 != 0:
            ll_filtered.append(num)
elif command == 'negative':
    for num in ll_unfiltered:
        if num < 0:
            ll_filtered.append(num)
elif command == 'positive':
    for num in ll_unfiltered:
        if num >= 0:
            ll_filtered.append(num)

print(ll_filtered)
