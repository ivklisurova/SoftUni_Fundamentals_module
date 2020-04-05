text = input().split('>')

final_text = ''

length_text = len(text)
counter = 1
left_symbols = 0

for word in text:
    if counter == 1:
        final_text += word
    else:
        length_word = len(word)
        symbols_to_remove = (int(word[0]) + left_symbols)
        if length_word < symbols_to_remove:
            left_symbols += (symbols_to_remove - length_word)

        new_word = word[symbols_to_remove:len(word)]
        final_text += new_word

        if length_word >= symbols_to_remove:
            left_symbols = 0

    if counter == length_text:
        break
    else:
        final_text += '>'
        counter += 1


print(final_text)