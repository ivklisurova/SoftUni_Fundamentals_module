string = input()
shuffle_count = int(input())

deck_cards = string.split()

current_deck = []

last_card = int(len(deck_cards) / 2)

for shuffle in range(shuffle_count):

    first_half = deck_cards[0:last_card]
    second_half = deck_cards[last_card:(len(deck_cards))]


    if shuffle != 0:
        current_deck.clear()

    for i in range(len(first_half)):
        for card_1 in first_half:
            current_deck.append(first_half[card_1])
        for card_2 in second_half:
            current_deck.append(second_half[card_2])



    deck_cards = current_deck

print(current_deck)
