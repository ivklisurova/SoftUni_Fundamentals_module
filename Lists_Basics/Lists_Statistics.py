n = int(input())

ll_positive = []
ll_negative = []

for i in range(n):
    num = int(input())
    if num >= 0:
        ll_positive.append(num)
    else:
        ll_negative.append(num)

st_1 = f'Count of positives: {len(ll_positive)}. '
st_2 = f'Sum of negatives: {sum(ll_negative)}'

print(ll_positive)
print(ll_negative)
print(f'{st_1}{st_2}')
