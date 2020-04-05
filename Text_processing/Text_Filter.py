def solve(ban_list, text):
    for word in ban_list:
        while word in text:
            text = text.replace(word, '*' * len(word))

    print(text)


solve(input().split(', '), input())
