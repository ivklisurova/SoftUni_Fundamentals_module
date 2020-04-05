def solve(text):
    emoticons = []
    for i, j in enumerate(text):
        if j == ':':
            emoticon = j + text[i + 1]
            emoticons.append(emoticon)
    return emoticons


def print_output(ll):
    [print(i) for i in ll]


print_output(solve(input()))
