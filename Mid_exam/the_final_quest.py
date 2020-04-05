words = input().split(' ')

a= len(words)

while True:
    tokens = input().split(' ')
    command = tokens[0]
    if command == 'Stop':
        break

    elif command == 'Delete':
        idx = int(tokens[1])
        if len(words) > idx >= 0:
            words.pop(idx + 1)

    elif command == 'Swap':
        word1 = tokens[1]
        word2 = tokens[2]
        if word1 and word2 in words:
            idx_word_1 = None
            idx_word_2 = None

            for i, j in enumerate(words):
                if j == word1:
                    idx_word_1 = int(i)
            for i, j in enumerate(words):
                if j == word2:
                    idx_word_2 = int(i)
            words[idx_word_1], words[idx_word_2] = words[idx_word_2], words[idx_word_1]

    elif command == 'Put':
        word = tokens[1]
        idx = int(tokens[2])
        if len(words) >= idx > 0:
            words.insert(idx - 1, word)

    elif command == 'Sort':
        words.sort(reverse=True)

    elif command == 'Replace':
        word_1 = tokens[1]
        word_2 = tokens[2]
        if word_2 in words:
            for x, y in enumerate(words):
                if y == word_2:
                    words.pop(x)
                    words.insert(x, word_1)

print(' '.join(words))
