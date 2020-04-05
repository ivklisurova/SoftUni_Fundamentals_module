miner_dict = {}

while True:
    command = input()
    if command == 'stop':
        break
    resource = command
    quantity = int(input())
    if resource not in miner_dict:
        miner_dict[resource] = 0
    miner_dict[resource] += quantity

[print(f'{key} -> {value}') for key, value in miner_dict.items()]
