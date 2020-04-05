def solve(text):
    text = text.split(':')
    text_to_search = text[1:]
    for i in text_to_search:
        emoticon = ':'
        emoticon += i[0]
        print(emoticon)


solve(input())
