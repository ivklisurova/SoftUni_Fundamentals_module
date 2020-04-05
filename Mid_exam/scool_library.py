library = input().split('&')

while True:
    tokens = input().split(' | ')
    command = tokens[0]
    if command == 'Done':
        break
    book = tokens[1]
    if command == 'Add Book':
        if book not in library:
            library.insert(0, book)
    elif command == 'Take Book':
        if book in library:
            library.remove(book)
    elif command == 'Swap Books':
        book_two = tokens[2]
        if book in library and book_two in library:
            idx_book = None
            idx_book_two = None
            for i, j in enumerate(library):
                if j == book:
                    idx_book = i
                elif j == book_two:
                    idx_book_two = i
            library[idx_book], library[idx_book_two] = library[idx_book_two], library[idx_book]
    elif command == 'Insert Book':
        library.append(book)
    elif command == 'Check Book':
        index = int(book)
        if 0 <= index < len(library):
            print(library[index])

print(', '.join(library))
