def add_to_deck(card, original_deck, n_deck):
    if card in original_deck:
        n_deck.append(card)
        return n_deck
    else:
        print('Card not found.')


def remove_from_deck(card, n_deck):
    if card in n_deck:
        n_deck.remove(card)
        return n_deck
    else:
        print('Card not found.')


def insert_in_deck(card, idx, n_deck):
    length_list = len(n_deck)

    if length_list >= idx >= 0 and card in deck:
        n_deck.insert(idx, card)
    else:
        print("Error!")


def swap_it(card_one, card_two, new_deck):
    idx_1_card = None
    idx_2_card = None

    for i, j in enumerate(new_deck):
        if j == card_one:
            idx_1_card = i
        if j == card_two:
            idx_2_card = i

    new_deck[idx_1_card], new_deck[idx_2_card] = new_deck[idx_2_card], new_deck[idx_1_card]

    return new_deck


deck = input().split(':')
new_deck = []

while True:
    command = input().split()

    action = command[0]

    if action == 'Ready':
        print(' '.join(new_deck))
        break

    elif action == 'Shuffle':
        card = command[1]
        new_deck = new_deck[::-1]

    elif action == 'Add':
        card = command[1]
        add_to_deck(card, deck, new_deck)

    elif action == 'Remove':
        card = command[1]
        remove_from_deck(card, new_deck)

    elif action == 'Insert':
        card = command[1]
        idx = int(command[2])
        insert_in_deck(card, idx, new_deck)

    elif action == 'Swap':
        card = command[1]
        card_2 = command[2]
        swap_it(card, card_2, new_deck)
