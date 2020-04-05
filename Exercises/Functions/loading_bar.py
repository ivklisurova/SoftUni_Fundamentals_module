def loading(num):
    positions = num // 10
    loading_bar = ['.'] * 10
    for i in range(positions):
        loading_bar[i] = '%'
    return loading_bar


number = int(input())

if number == 100:
    print(f"100% Complete!\n[{''.join(loading(number))}]")
else:
    print(f"{number}% [{''.join(loading(number))}]\nStill loading...")

