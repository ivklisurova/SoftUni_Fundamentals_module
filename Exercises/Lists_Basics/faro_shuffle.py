deck = input().split()
shuffles = int(input())

new_deck = deck

for i in range(shuffles):
    mid = len(new_deck) // 2
    first_half = new_deck[:mid]
    second_half = new_deck[mid:]
    zipped = list(zip(first_half, second_half))
    new_deck.clear()
    for x, y in zipped:
        new_deck.append(x)
        new_deck.append(y)

print(new_deck)
