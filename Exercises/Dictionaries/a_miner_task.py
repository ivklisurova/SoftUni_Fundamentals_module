resources = {}

while True:
    tokens = input()
    if tokens == 'stop':
        break
    quantity = int(input())
    if tokens not in resources:
        resources[tokens] = 0
    resources[tokens] += quantity

for k, v in resources.items():
    print(f'{k} -> {v}')
